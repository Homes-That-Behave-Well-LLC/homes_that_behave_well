"""Pure record/schema regressions, separate from HA runtime fixture coverage."""

from dataclasses import replace
from types import SimpleNamespace
from unittest.mock import Mock, patch

import probatio
import pytest
from homeassistant.components.diagnostics import REDACTED

from custom_components.htbw.config_flow import (
    _assignments_from_user_input,
    _build_initial_schema,
    _build_options_schema,
)
from custom_components.htbw.const import (
    CONF_ASSIGNMENTS,
    AssignmentResolution,
    InteractionFunction,
    ParticipationState,
    ReferenceType,
)
from custom_components.htbw.diagnostics import async_get_config_entry_diagnostics
from custom_components.htbw.foundation import get_room_interaction_assignments
from custom_components.htbw.models import HTBWRuntimeData, RoomInteractionFunctionAssignment


def _record(reference: str, state: ParticipationState) -> RoomInteractionFunctionAssignment:
    return RoomInteractionFunctionAssignment(
        room_id="configured_room",
        function=InteractionFunction.SPOKEN_RESPONSE_OUTPUT,
        reference_type=ReferenceType.ENTITY_ID,
        reference_id=reference,
        participation_state=state,
        assigned_at="2026-01-01T00:00:00+00:00",
        updated_at="2026-01-02T00:00:00+00:00",
    )


def test_native_schemas_validate_multiple_references() -> None:
    initial = _build_initial_schema()
    data = {
        "area_id": "configured_room",
        "spoken_response_output": ["media_player.first", "media_player.second"],
    }
    assert initial(data) == data
    with pytest.raises(probatio.Invalid):
        initial({"area_id": "configured_room", "spoken_response_output": "media_player.first"})
    with pytest.raises(probatio.Invalid):
        initial({"area_id": "configured_room", "spoken_response_output": ["sensor.not_output"]})

    options = _build_options_schema({})
    selections = {
        "voice_input": ["assist_satellite.input"],
        "spoken_response_output": ["media_player.output"],
        "interface": ["native_device_id"],
        "physical_remote": ["remote.controller", "event.key", "button.action"],
        "voice_input_devices": ["native_input"],
        "spoken_response_output_devices": ["native_output"],
        "physical_remote_devices": ["native_remote"],
    }
    grouped = {
        "voice_input": {
            "voice_input": selections["voice_input"],
            "voice_input_devices": selections["voice_input_devices"],
        },
        "spoken_response_output": {
            "spoken_response_output": selections["spoken_response_output"],
            "spoken_response_output_devices": selections["spoken_response_output_devices"],
        },
        "interface": {"interface": selections["interface"]},
        "physical_remote": {
            "physical_remote": selections["physical_remote"],
            "physical_remote_devices": selections["physical_remote_devices"],
        },
    }
    assert options(grouped) == grouped
    assert options({}) == {}
    records = _assignments_from_user_input("configured_room", selections)
    assert len(records) == 9
    assert sum(a.reference_type is ReferenceType.DEVICE_ID for a in records) == 4
    assert {a.function for a in records} == set(InteractionFunction)


def test_record_roundtrip_preserves_every_participation_state() -> None:
    for state in ParticipationState:
        original = _record("media_player.output", state)
        assert RoomInteractionFunctionAssignment.from_dict(original.to_dict()) == original
    incomplete = _record("media_player.output", ParticipationState.PARTICIPATING).to_dict()
    del incomplete["assigned_at"]
    with pytest.raises(KeyError):
        RoomInteractionFunctionAssignment.from_dict(incomplete)


def test_options_keep_atomic_records_and_original_timestamps() -> None:
    records = [
        _record("media_player.first", ParticipationState.PARTICIPATING),
        _record("media_player.second", ParticipationState.PARTICIPATING),
        _record("media_player.excluded", ParticipationState.DELIBERATELY_EXCLUDED),
    ]
    result = _assignments_from_user_input(
        "configured_room",
        {"spoken_response_output": ["media_player.first", "media_player.second"]},
        records,
    )
    assert result == records
    assert len(result) == 3
    assert all(isinstance(record.reference_id, str) for record in result)


def test_clear_and_explicit_reactivation_preserve_participation_metadata() -> None:
    active = _record("media_player.active", ParticipationState.PARTICIPATING)
    excluded = _record("media_player.excluded", ParticipationState.DELIBERATELY_EXCLUDED)
    assert _assignments_from_user_input("configured_room", {}, [active, excluded]) == [excluded]
    (reactivated,) = _assignments_from_user_input(
        "configured_room", {"spoken_response_output": [excluded.reference_id]}, [excluded]
    )
    assert reactivated.participation_state is ParticipationState.PARTICIPATING
    assert reactivated.reference_id == excluded.reference_id
    assert reactivated.assigned_at == excluded.assigned_at
    assert reactivated.updated_at != excluded.updated_at


def test_options_do_not_collapse_existing_records_with_the_same_reference() -> None:
    first = _record("media_player.shared_reference", ParticipationState.PARTICIPATING)
    second = replace(
        first,
        assigned_at="2026-01-03T00:00:00+00:00",
        updated_at="2026-01-03T00:00:00+00:00",
    )
    assert _assignments_from_user_input(
        "configured_room", {"spoken_response_output": [first.reference_id]}, [first, second]
    ) == [first, second]


def test_lookup_does_not_select_one_record_or_return_excluded_records() -> None:
    missing = _record("media_player.missing", ParticipationState.PARTICIPATING)
    present = _record("media_player.present", ParticipationState.PARTICIPATING)
    excluded = _record("media_player.excluded", ParticipationState.DELIBERATELY_EXCLUDED)
    hass = Mock()
    hass.config_entries.async_entries.return_value = [
        SimpleNamespace(runtime_data=HTBWRuntimeData([missing, excluded, present]))
    ]
    with patch(
        "custom_components.htbw.foundation.reference_exists",
        side_effect=lambda _hass, _type, reference: reference == present.reference_id,
    ) as exists:
        results = get_room_interaction_assignments(
            hass, "configured_room", InteractionFunction.SPOKEN_RESPONSE_OUTPUT
        )
    assert [r.assignment for r in results] == [missing, present]
    assert [r.status for r in results] == [
        AssignmentResolution.MISSING,
        AssignmentResolution.RESOLVED,
    ]
    assert exists.call_count == 2
    assert (
        get_room_interaction_assignments(
            hass, "another_room", InteractionFunction.SPOKEN_RESPONSE_OUTPUT
        )
        == []
    )


async def test_diagnostics_redact_identifiers_and_do_not_export_extra_data() -> None:
    record = _record("media_player.private_reference", ParticipationState.DELIBERATELY_EXCLUDED)
    entry = Mock()
    entry.entry_id = "private_entry"
    entry.data = {"room_id": "private_room", "token": "synthetic_do_not_export"}
    entry.options = {"password": "another_synthetic_value", CONF_ASSIGNMENTS: [record.to_dict()]}
    del entry.runtime_data
    with patch("custom_components.htbw.diagnostics.reference_exists", return_value=False):
        result = await async_get_config_entry_diagnostics(Mock(), entry)
    assert result["room_id"] == REDACTED
    assert result["config_entry_id"] == REDACTED
    (assignment,) = result["assignments"]
    assert assignment["reference_id"] == REDACTED
    assert assignment["reference_exists"] is False
    assert assignment["standing_defect"] is False
    for private_value in (
        "private_entry",
        "private_room",
        record.reference_id,
        "synthetic_do_not_export",
        "another_synthetic_value",
    ):
        assert private_value not in str(result)
