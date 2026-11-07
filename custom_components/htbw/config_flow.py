"""Config and options flow for HTBW Core.

Implements SS5 (Foundation Room Setup requirements), SS4.1 (atomic records),
and SS18 (native selectors) of
docs/architecture/foundation-room-interaction-roles-specification.md.

One config entry represents one Room's full set of Interaction Function
Assignments. Multiple Rooms are supported by adding multiple config entries.

The initial flow collects the native Area (Room) context plus the two
historically-integrated functions (voice_input, spoken_response_output) in
one step, so optional setup does not block an initial, minimal
configuration. `interface` and `physical_remote` are configured afterwards
through the Options flow, consistent with "do not make optional functions
block initial setup."
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import replace
from typing import Any

import probatio
from homeassistant.config_entries import ConfigEntry, ConfigFlow, ConfigFlowResult, OptionsFlow
from homeassistant.core import callback
from homeassistant.helpers import area_registry as ar
from homeassistant.helpers import selector

from .const import (
    CONF_ASSIGNMENTS,
    CONF_ROOM_ID,
    DOMAIN,
    InteractionFunction,
    ParticipationState,
    ReferenceType,
)
from .models import RoomInteractionFunctionAssignment
from .storage import load_assignments

CONF_VOICE_INPUT = InteractionFunction.VOICE_INPUT.value
CONF_SPOKEN_RESPONSE_OUTPUT = InteractionFunction.SPOKEN_RESPONSE_OUTPUT.value
CONF_INTERFACE = InteractionFunction.INTERFACE.value
CONF_PHYSICAL_REMOTE = InteractionFunction.PHYSICAL_REMOTE.value
CONF_VOICE_INPUT_DEVICES = "voice_input_devices"
CONF_SPOKEN_RESPONSE_OUTPUT_DEVICES = "spoken_response_output_devices"
CONF_PHYSICAL_REMOTE_DEVICES = "physical_remote_devices"

_FIELD_REFERENCES = {
    CONF_VOICE_INPUT: (InteractionFunction.VOICE_INPUT, ReferenceType.ENTITY_ID),
    CONF_SPOKEN_RESPONSE_OUTPUT: (
        InteractionFunction.SPOKEN_RESPONSE_OUTPUT,
        ReferenceType.ENTITY_ID,
    ),
    CONF_INTERFACE: (InteractionFunction.INTERFACE, ReferenceType.DEVICE_ID),
    CONF_PHYSICAL_REMOTE: (InteractionFunction.PHYSICAL_REMOTE, ReferenceType.ENTITY_ID),
    CONF_VOICE_INPUT_DEVICES: (InteractionFunction.VOICE_INPUT, ReferenceType.DEVICE_ID),
    CONF_SPOKEN_RESPONSE_OUTPUT_DEVICES: (
        InteractionFunction.SPOKEN_RESPONSE_OUTPUT,
        ReferenceType.DEVICE_ID,
    ),
    CONF_PHYSICAL_REMOTE_DEVICES: (InteractionFunction.PHYSICAL_REMOTE, ReferenceType.DEVICE_ID),
}


def _build_initial_schema() -> probatio.Schema:
    return probatio.Schema(
        {
            probatio.Required("area_id"): selector.AreaSelector(selector.AreaSelectorConfig()),
            probatio.Optional(CONF_VOICE_INPUT): selector.EntitySelector(
                selector.EntitySelectorConfig(multiple=True)
            ),
            probatio.Optional(CONF_SPOKEN_RESPONSE_OUTPUT): selector.EntitySelector(
                selector.EntitySelectorConfig(domain="media_player", multiple=True)
            ),
        }
    )


def _build_options_schema(current: dict[str, list[str]]) -> probatio.Schema:
    return probatio.Schema(
        {
            probatio.Optional(
                CONF_VOICE_INPUT,
                description={"suggested_value": current.get(CONF_VOICE_INPUT)},
            ): selector.EntitySelector(selector.EntitySelectorConfig(multiple=True)),
            probatio.Optional(
                CONF_SPOKEN_RESPONSE_OUTPUT,
                description={"suggested_value": current.get(CONF_SPOKEN_RESPONSE_OUTPUT)},
            ): selector.EntitySelector(
                selector.EntitySelectorConfig(domain="media_player", multiple=True)
            ),
            probatio.Optional(
                CONF_INTERFACE,
                description={"suggested_value": current.get(CONF_INTERFACE)},
            ): selector.DeviceSelector(selector.DeviceSelectorConfig(multiple=True)),
            probatio.Optional(
                CONF_PHYSICAL_REMOTE,
                description={"suggested_value": current.get(CONF_PHYSICAL_REMOTE)},
            ): selector.EntitySelector(
                selector.EntitySelectorConfig(domain=["remote", "event", "button"], multiple=True)
            ),
            **{
                probatio.Optional(
                    key, description={"suggested_value": current.get(key)}
                ): selector.DeviceSelector(selector.DeviceSelectorConfig(multiple=True))
                for key in (
                    CONF_VOICE_INPUT_DEVICES,
                    CONF_SPOKEN_RESPONSE_OUTPUT_DEVICES,
                    CONF_PHYSICAL_REMOTE_DEVICES,
                )
            },
        }
    )


def _assignments_from_user_input(
    room_id: str,
    user_input: dict[str, Any],
    current: list[RoomInteractionFunctionAssignment] | None = None,
) -> list[RoomInteractionFunctionAssignment]:
    """Build assignment records from selector output.

    Only functions the resident actually selected a reference for become
    records -- an omitted/cleared function is simply absent, never a
    silently-inferred assignment (spec SS5 "no silent assignment"; SS6).
    """
    previous: dict[
        tuple[InteractionFunction, ReferenceType, str], list[RoomInteractionFunctionAssignment]
    ] = defaultdict(list)
    for assignment in current or []:
        previous[(assignment.function, assignment.reference_type, assignment.reference_id)].append(
            assignment
        )
    assignments: list[RoomInteractionFunctionAssignment] = []
    selected: set[tuple[InteractionFunction, ReferenceType, str]] = set()
    for field, (function, reference_type) in _FIELD_REFERENCES.items():
        for reference_id in dict.fromkeys(user_input.get(field, [])):
            key = (function, reference_type, reference_id)
            selected.add(key)
            old_records = previous.get(key, [])
            assignment = RoomInteractionFunctionAssignment(
                room_id=room_id,
                function=function,
                reference_type=reference_type,
                reference_id=reference_id,
            )
            if old_records:
                assignments.extend(
                    old
                    if old.participation_state is ParticipationState.PARTICIPATING
                    else replace(assignment, assigned_at=old.assigned_at)
                    for old in old_records
                )
            else:
                assignments.append(assignment)
    assignments.extend(
        a
        for a in current or []
        if a.participation_state is not ParticipationState.PARTICIPATING
        and (a.function, a.reference_type, a.reference_id) not in selected
    )
    return assignments


class HTBWConfigFlow(ConfigFlow, domain=DOMAIN):
    """Config flow for HTBW Core -- one Room's Interaction Function Assignments."""

    VERSION = 1

    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult:
        """First and only required setup step.

        Collects the native Area (Room) reference and, optionally, the two
        historically-integrated functions. `interface` and `physical_remote`
        are configured afterward through the Options flow (spec SS5: "do
        not make optional functions block initial setup").
        """
        errors: dict[str, str] = {}

        if user_input is not None:
            area_id = user_input["area_id"]
            await self.async_set_unique_id(area_id)
            self._abort_if_unique_id_configured()

            area_registry = ar.async_get(self.hass)
            area_entry = area_registry.async_get_area(area_id)
            if area_entry is None:
                errors["area_id"] = "area_not_found"
            else:
                assignments = _assignments_from_user_input(area_id, user_input)
                return self.async_create_entry(
                    title=area_entry.name,
                    data={CONF_ROOM_ID: area_id},
                    options={CONF_ASSIGNMENTS: [a.to_dict() for a in assignments]},
                )

        return self.async_show_form(
            step_id="user",
            data_schema=_build_initial_schema(),
            errors=errors,
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> HTBWOptionsFlow:
        """Return this integration's options flow."""
        return HTBWOptionsFlow()


class HTBWOptionsFlow(OptionsFlow):
    """Options flow: add, change, or remove participating assignments (spec SS5).

    Also the sole configuration surface for the two optional functions,
    `interface` and `physical_remote`.
    """

    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult:
        """Reconfigure any of the four Interaction Function Assignments."""
        room_id = self.config_entry.data[CONF_ROOM_ID]
        current_assignments = load_assignments(self.config_entry)
        current_by_field: dict[str, list[str]] = {
            field: [
                a.reference_id
                for a in current_assignments
                if a.function is function
                and a.reference_type is reference_type
                and a.participation_state is ParticipationState.PARTICIPATING
            ]
            for field, (function, reference_type) in _FIELD_REFERENCES.items()
        }
        errors: dict[str, str] = {}
        for assignment in current_assignments:
            if assignment.participation_state is not ParticipationState.PARTICIPATING:
                continue
            if (assignment.function, assignment.reference_type) not in _FIELD_REFERENCES.values():
                errors["base"] = "unsupported_reference_type"

        if user_input is not None and not errors:
            assignments = _assignments_from_user_input(room_id, user_input, current_assignments)
            return self.async_create_entry(
                title="",
                data={CONF_ASSIGNMENTS: [a.to_dict() for a in assignments]},
            )

        return self.async_show_form(
            step_id="init",
            data_schema=_build_options_schema(current_by_field),
            errors=errors,
        )
