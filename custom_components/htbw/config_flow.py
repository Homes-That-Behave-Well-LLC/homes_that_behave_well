"""Config and options flow for HTBW Core.

Implements SS5 (Foundation Room Setup requirements), SS7 (native selectors),
SS19 (config flow), and SS20 (options/reconfiguration) of
docs/architecture/foundation-room-interaction-roles-specification.md.

One config entry represents one Room's full set of Interaction Function
Assignments (a deliberate, documented v1 boundary -- see the implementation
report for Issue #201, SS21). Multiple Rooms are supported by adding
multiple config entries.

The initial flow collects the native Area (Room) context plus the two
historically-integrated functions (voice_input, spoken_response_output) in
one step, so optional setup does not block an initial, minimal
configuration. `interface` and `physical_remote` are configured afterwards
through the Options flow, consistent with "do not make optional functions
block initial setup."
"""

from __future__ import annotations

from typing import Any

import voluptuous as vol
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

CONF_VOICE_INPUT = InteractionFunction.VOICE_INPUT.value
CONF_SPOKEN_RESPONSE_OUTPUT = InteractionFunction.SPOKEN_RESPONSE_OUTPUT.value
CONF_INTERFACE = InteractionFunction.INTERFACE.value
CONF_PHYSICAL_REMOTE = InteractionFunction.PHYSICAL_REMOTE.value


def _build_initial_schema() -> vol.Schema:
    return vol.Schema(
        {
            vol.Required("area_id"): selector.AreaSelector(
                selector.AreaSelectorConfig()
            ),
            vol.Optional(CONF_VOICE_INPUT): selector.EntitySelector(
                selector.EntitySelectorConfig()
            ),
            vol.Optional(CONF_SPOKEN_RESPONSE_OUTPUT): selector.EntitySelector(
                selector.EntitySelectorConfig(domain="media_player")
            ),
        }
    )


def _build_options_schema(current: dict[str, str]) -> vol.Schema:
    return vol.Schema(
        {
            vol.Optional(
                CONF_VOICE_INPUT,
                description={"suggested_value": current.get(CONF_VOICE_INPUT)},
            ): selector.EntitySelector(selector.EntitySelectorConfig()),
            vol.Optional(
                CONF_SPOKEN_RESPONSE_OUTPUT,
                description={"suggested_value": current.get(CONF_SPOKEN_RESPONSE_OUTPUT)},
            ): selector.EntitySelector(selector.EntitySelectorConfig(domain="media_player")),
            vol.Optional(
                CONF_INTERFACE,
                description={"suggested_value": current.get(CONF_INTERFACE)},
            ): selector.DeviceSelector(selector.DeviceSelectorConfig()),
            vol.Optional(
                CONF_PHYSICAL_REMOTE,
                description={"suggested_value": current.get(CONF_PHYSICAL_REMOTE)},
            ): selector.EntitySelector(
                selector.EntitySelectorConfig(domain=["remote", "event", "button"])
            ),
        }
    )


def _assignments_from_user_input(
    room_id: str, user_input: dict[str, Any]
) -> list[RoomInteractionFunctionAssignment]:
    """Build assignment records from selector output.

    Only functions the resident actually selected a reference for become
    records -- an omitted/cleared function is simply absent, never a
    silently-inferred assignment (spec SS5 "no silent assignment"; SS6).
    """
    assignments: list[RoomInteractionFunctionAssignment] = []

    def _add(function: InteractionFunction, reference_type: ReferenceType, key: str) -> None:
        value = user_input.get(key)
        if not value:
            return
        assignments.append(
            RoomInteractionFunctionAssignment(
                room_id=room_id,
                function=function,
                reference_type=reference_type,
                reference_id=value,
                participation_state=ParticipationState.PARTICIPATING,
            )
        )

    _add(InteractionFunction.VOICE_INPUT, ReferenceType.ENTITY_ID, CONF_VOICE_INPUT)
    _add(
        InteractionFunction.SPOKEN_RESPONSE_OUTPUT,
        ReferenceType.ENTITY_ID,
        CONF_SPOKEN_RESPONSE_OUTPUT,
    )
    _add(InteractionFunction.INTERFACE, ReferenceType.DEVICE_ID, CONF_INTERFACE)
    _add(InteractionFunction.PHYSICAL_REMOTE, ReferenceType.ENTITY_ID, CONF_PHYSICAL_REMOTE)
    return assignments


class HTBWConfigFlow(ConfigFlow, domain=DOMAIN):
    """Config flow for HTBW Core -- one Room's Interaction Function Assignments."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """First and only required setup step.

        Collects the native Area (Room) reference and, optionally, the two
        historically-integrated functions. `interface` and `physical_remote`
        are configured afterward through the Options flow (spec SS19: "do
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
    """Options flow: add, change, or remove an assignment (spec SS20).

    Also the sole configuration surface for the two optional functions,
    `interface` and `physical_remote`.
    """

    async def async_step_init(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Reconfigure any of the four Interaction Function Assignments."""
        room_id = self.config_entry.data[CONF_ROOM_ID]
        current_raw = self.config_entry.options.get(CONF_ASSIGNMENTS, [])
        current_assignments = [
            RoomInteractionFunctionAssignment.from_dict(item) for item in current_raw
        ]
        current_by_function = {a.function.value: a.reference_id for a in current_assignments}

        if user_input is not None:
            assignments = _assignments_from_user_input(room_id, user_input)
            return self.async_create_entry(
                title="",
                data={CONF_ASSIGNMENTS: [a.to_dict() for a in assignments]},
            )

        return self.async_show_form(
            step_id="init",
            data_schema=_build_options_schema(current_by_function),
        )
