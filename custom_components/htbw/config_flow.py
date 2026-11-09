"""Config, options, and Room subentry flows for HTBW Core.

Configuration hierarchy (Issue #162, Owner decision B):

- One household HTBW config entry: the Integration configuration authority. It
  holds household/Integration-scoped settings only -- "Retain Enrollment
  Recordings" (DL-145 SS2, placed in the Integration Options Flow by DL-148)
  and the Voice Evidence App connection provisioned by Supervisor Discovery.
- One native config subentry per HTBW Room: the Room Configuration authority.
  Implements SS5 (Foundation Room Setup requirements), SS4.1 (atomic records),
  and SS18 (native selectors) of
  docs/architecture/foundation-room-interaction-roles-specification.md exactly
  as #201 did; only the persistence carrier changed.

Adding a Room collects the native Area context plus the two
historically-integrated functions (voice_input, spoken_response_output), so
optional setup does not block an initial, minimal configuration. `interface`
and `physical_remote` are configured afterwards by reconfiguring the Room,
consistent with "do not make optional functions block initial setup."
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import replace
from typing import Any

import probatio
from homeassistant.config_entries import (
    ConfigEntry,
    ConfigFlow,
    ConfigFlowResult,
    ConfigSubentryFlow,
    OptionsFlow,
    SubentryFlowResult,
)
from homeassistant.core import callback
from homeassistant.data_entry_flow import section
from homeassistant.helpers import area_registry as ar
from homeassistant.helpers import selector
from homeassistant.helpers.service_info.hassio import HassioServiceInfo

from .const import (
    CONF_API_SECRET,
    CONF_APP_SLUG,
    CONF_EXTERNAL_STORAGE_PATH,
    CONF_HOST,
    CONF_PORT,
    CONF_RETAIN_ENROLLMENT_RECORDINGS,
    CONF_ROOM_ID,
    CONF_VOICE_EVIDENCE,
    DOMAIN,
    HOUSEHOLD_TITLE,
    HOUSEHOLD_UNIQUE_ID,
    RETENTION_DELETE,
    RETENTION_RETAIN,
    SUBENTRY_TYPE_ROOM,
    InteractionFunction,
    ParticipationState,
    ReferenceType,
)
from .models import RoomInteractionFunctionAssignment
from .storage import load_assignments, room_subentries, room_subentry_data

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
    fields = probatio.Schema(
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
    return probatio.Schema(
        {
            probatio.Optional(function.value): section(
                probatio.Schema(
                    {
                        key: value
                        for key, value in fields.schema.items()
                        if _FIELD_REFERENCES[key.schema][0] is function
                    }
                ),
                {"collapsed": False},
            )
            for function in InteractionFunction
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


def _retention_schema(default: str | None = None) -> probatio.Schema:
    """The household's explicit DL-145 choice; deliberately no implicit default."""
    key = (
        probatio.Required(CONF_RETAIN_ENROLLMENT_RECORDINGS, default=default)
        if default is not None
        else probatio.Required(CONF_RETAIN_ENROLLMENT_RECORDINGS)
    )
    return probatio.Schema(
        {
            key: selector.SelectSelector(
                selector.SelectSelectorConfig(
                    options=[RETENTION_RETAIN, RETENTION_DELETE],
                    translation_key="retain_enrollment_recordings",
                    mode=selector.SelectSelectorMode.LIST,
                )
            )
        }
    )


def _options_schema(
    retention_default: str | None, external_storage_path_default: str | None
) -> probatio.Schema:
    """Household options: DL-145 retention plus the optional #211 External Storage path."""
    retention_key = (
        probatio.Required(CONF_RETAIN_ENROLLMENT_RECORDINGS, default=retention_default)
        if retention_default is not None
        else probatio.Required(CONF_RETAIN_ENROLLMENT_RECORDINGS)
    )
    storage_key = probatio.Optional(
        CONF_EXTERNAL_STORAGE_PATH, default=external_storage_path_default or ""
    )
    return probatio.Schema(
        {
            retention_key: selector.SelectSelector(
                selector.SelectSelectorConfig(
                    options=[RETENTION_RETAIN, RETENTION_DELETE],
                    translation_key="retain_enrollment_recordings",
                    mode=selector.SelectSelectorMode.LIST,
                )
            ),
            storage_key: selector.TextSelector(),
        }
    )


def _discovery_connection(discovery_info: HassioServiceInfo) -> dict[str, Any] | None:
    """Validate a Supervisor Discovery payload into the stored App connection."""
    config = discovery_info.config
    host, port, secret = config.get(CONF_HOST), config.get(CONF_PORT), config.get(CONF_API_SECRET)
    if not isinstance(host, str) or not host or not isinstance(secret, str) or len(secret) < 32:
        return None
    try:
        port_number = int(port)  # type: ignore[arg-type]
    except TypeError, ValueError:
        return None
    if not 0 < port_number < 65536:
        return None
    return {
        CONF_HOST: host,
        CONF_PORT: port_number,
        CONF_API_SECRET: secret,
        CONF_APP_SLUG: discovery_info.slug,
    }


def _current_by_field(
    assignments: list[RoomInteractionFunctionAssignment],
) -> dict[str, list[str]]:
    return {
        field: [
            a.reference_id
            for a in assignments
            if a.function is function
            and a.reference_type is reference_type
            and a.participation_state is ParticipationState.PARTICIPATING
        ]
        for field, (function, reference_type) in _FIELD_REFERENCES.items()
    }


class HTBWConfigFlow(ConfigFlow, domain=DOMAIN):
    """Config flow for the single household HTBW entry."""

    VERSION = 2
    MINOR_VERSION = 1

    def __init__(self) -> None:
        """Initialize the flow."""
        self._discovered_connection: dict[str, Any] | None = None

    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult:
        """Create the household HTBW entry, recording the DL-145 retention choice first."""
        await self.async_set_unique_id(HOUSEHOLD_UNIQUE_ID)
        self._abort_if_unique_id_configured()
        if user_input is not None:
            return self.async_create_entry(
                title=HOUSEHOLD_TITLE,
                data={},
                options={
                    CONF_RETAIN_ENROLLMENT_RECORDINGS: user_input[CONF_RETAIN_ENROLLMENT_RECORDINGS]
                },
            )
        return self.async_show_form(step_id="user", data_schema=_retention_schema())

    async def async_step_hassio(self, discovery_info: HassioServiceInfo) -> ConfigFlowResult:
        """Bind the Supervisor-discovered Voice Evidence App to the household entry.

        Idempotent: repeated discovery (including after secret rotation)
        reconciles the one household entry's App connection and never creates
        a second HTBW entry. The secret is never logged.
        """
        connection = _discovery_connection(discovery_info)
        if connection is None:
            return self.async_abort(reason="invalid_discovery_info")
        await self.async_set_unique_id(HOUSEHOLD_UNIQUE_ID)
        self._abort_if_unique_id_configured(updates={CONF_VOICE_EVIDENCE: connection})
        self._discovered_connection = connection
        return await self.async_step_hassio_confirm()

    async def async_step_hassio_confirm(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Create the household entry from discovery; the retention choice is required first."""
        assert self._discovered_connection is not None
        if user_input is not None:
            return self.async_create_entry(
                title=HOUSEHOLD_TITLE,
                data={CONF_VOICE_EVIDENCE: self._discovered_connection},
                options={
                    CONF_RETAIN_ENROLLMENT_RECORDINGS: user_input[CONF_RETAIN_ENROLLMENT_RECORDINGS]
                },
            )
        return self.async_show_form(step_id="hassio_confirm", data_schema=_retention_schema())

    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> HTBWOptionsFlow:
        """Return the household (Integration-scoped) options flow."""
        return HTBWOptionsFlow()

    @classmethod
    @callback
    def async_get_supported_subentry_types(
        cls, config_entry: ConfigEntry
    ) -> dict[str, type[ConfigSubentryFlow]]:
        """Rooms are native config subentries of the household entry."""
        return {SUBENTRY_TYPE_ROOM: RoomSubentryFlow}


class HTBWOptionsFlow(OptionsFlow):
    """Household/Integration-scoped options only. Room settings never appear here."""

    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult:
        """Change "Retain Enrollment Recordings" (DL-145) and External Storage (#211, DL-151).

        External Storage asks only for the path HTBW should use beneath the
        household's already Home-Assistant-managed Share-usage connection --
        never NAS credentials, protocol, or mount options (DL-151 SS7). The
        path is validated against ``hass.config.is_allowed_path()`` (current
        official Home Assistant security guidance), and a household that has
        not yet added it to their own ``allowlist_external_dirs`` is told so
        directly, inline, rather than accepted silently.
        """
        errors: dict[str, str] = {}
        current_path = self.config_entry.options.get(CONF_EXTERNAL_STORAGE_PATH)
        if user_input is not None:
            path = user_input.get(CONF_EXTERNAL_STORAGE_PATH, "").strip()
            if path:
                allowed = await self.hass.async_add_executor_job(
                    self.hass.config.is_allowed_path, path
                )
                if not allowed:
                    errors[CONF_EXTERNAL_STORAGE_PATH] = "path_not_allowed"
            if not errors:
                return self.async_create_entry(
                    title="",
                    data={
                        **self.config_entry.options,
                        CONF_RETAIN_ENROLLMENT_RECORDINGS: user_input[
                            CONF_RETAIN_ENROLLMENT_RECORDINGS
                        ],
                        CONF_EXTERNAL_STORAGE_PATH: path,
                    },
                )
        return self.async_show_form(
            step_id="init",
            data_schema=_options_schema(
                self.config_entry.options.get(CONF_RETAIN_ENROLLMENT_RECORDINGS),
                current_path,
            ),
            errors=errors,
        )


class RoomSubentryFlow(ConfigSubentryFlow):
    """Add or reconfigure one HTBW Room's Interaction Function Assignments."""

    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> SubentryFlowResult:
        """Add a Room (spec SS5): Area plus the two historically-integrated functions."""
        errors: dict[str, str] = {}
        if user_input is not None:
            area_id = user_input["area_id"]
            entry = self._get_entry()
            if any(s.unique_id == area_id for s in room_subentries(entry)):
                return self.async_abort(reason="already_configured")
            area_entry = ar.async_get(self.hass).async_get_area(area_id)
            if area_entry is None:
                errors["area_id"] = "area_not_found"
            else:
                assignments = _assignments_from_user_input(area_id, user_input)
                return self.async_create_entry(
                    title=area_entry.name,
                    data=room_subentry_data(area_id, assignments),
                    unique_id=area_id,
                )

        return self.async_show_form(
            step_id="user", data_schema=_build_initial_schema(), errors=errors
        )

    async def async_step_reconfigure(
        self, user_input: dict[str, Any] | None = None
    ) -> SubentryFlowResult:
        """Reconfigure any of the four Interaction Function Assignments (spec SS5)."""
        entry = self._get_entry()
        subentry = self._get_reconfigure_subentry()
        room_id = subentry.data[CONF_ROOM_ID]
        current_assignments = load_assignments(subentry)
        errors: dict[str, str] = {}
        for assignment in current_assignments:
            if assignment.participation_state is not ParticipationState.PARTICIPATING:
                continue
            if (assignment.function, assignment.reference_type) not in _FIELD_REFERENCES.values():
                errors["base"] = "unsupported_reference_type"

        if user_input is not None and not errors:
            # Sections change only the form payload, not the persisted assignment shape.
            selections = {
                field: user_input.get(function.value, {}).get(field, [])
                for field, (function, _) in _FIELD_REFERENCES.items()
            }
            assignments = _assignments_from_user_input(room_id, selections, current_assignments)
            return self.async_update_and_abort(
                entry, subentry, data=room_subentry_data(room_id, assignments)
            )

        return self.async_show_form(
            step_id="reconfigure",
            data_schema=_build_options_schema(_current_by_field(current_assignments)),
            errors=errors,
        )
