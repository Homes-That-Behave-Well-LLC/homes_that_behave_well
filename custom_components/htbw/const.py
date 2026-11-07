"""Constants for the HTBW Core integration.

Implements the accepted vocabulary from
docs/architecture/foundation-room-interaction-roles-specification.md and
DL-87, DL-88, DL-90, DL-91 (Issues #195, #198, #196, #199, all closed).
Nothing in this module introduces new architecture; it restates accepted
terms as Python constants/enums only.
"""

from __future__ import annotations

from enum import StrEnum

DOMAIN = "htbw"

# Config entry data/options keys.
CONF_ROOM_ID = "room_id"
CONF_ASSIGNMENTS = "assignments"


class InteractionFunction(StrEnum):
    """The four accepted Interaction Function Assignment roles (DL-88).

    Exactly these four values are accepted. Do not add aliases such as
    "speaker", "microphone", "display", or "remote_control" -- the
    canonical vocabulary is restated here, not reinterpreted.
    """

    VOICE_INPUT = "voice_input"
    SPOKEN_RESPONSE_OUTPUT = "spoken_response_output"
    INTERFACE = "interface"
    PHYSICAL_REMOTE = "physical_remote"


class ReferenceType(StrEnum):
    """Native Home Assistant reference types (DL-87 rank 1, spec SS4.1/SS18.1).

    A RoomInteractionFunctionAssignment's participating_capability_reference
    is always one of these two native identifier kinds -- never a display
    name, IP address, hostname, or vendor-specific identifier.
    """

    ENTITY_ID = "entity_id"
    DEVICE_ID = "device_id"


class ParticipationState(StrEnum):
    """Room Configuration's existing three-state participation model.

    Restated unchanged from room-configuration.md / room-configuration-contract.md;
    this integration does not invent a fourth state.
    """

    PARTICIPATING = "participating"
    NOT_SELECTED = "not_selected"
    DELIBERATELY_EXCLUDED = "deliberately_excluded"


class AssignmentResolution(StrEnum):
    """Existence-only outcome for a participating record (spec SS7/SS8).
    RESOLVED: a record exists and its stored native reference still exists
        in the relevant Home Assistant registry. This is an existence
        check only -- it never asserts current runtime availability
        (on/off, reachable, powered); that remains a separate, later
        runtime concern outside Foundation's Truth boundary.
    MISSING: a record exists but its stored native reference no longer
        resolves in the registry -- a standing, Repairs-eligible defect.
    """

    RESOLVED = "resolved"
    MISSING = "missing"


# Prefix also identifies legacy per-function issues for reconciliation.
ISSUE_ID_PREFIX = "missing_reference_{entry_id}_"
