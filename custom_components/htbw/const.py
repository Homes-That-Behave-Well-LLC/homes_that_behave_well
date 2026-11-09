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

# Configuration hierarchy (Issue #162, Owner decision B): exactly one household
# HTBW config entry is the Integration configuration authority; each HTBW Room
# is a native config subentry beneath it (Room Configuration authority).
HOUSEHOLD_UNIQUE_ID = "htbw_household"
HOUSEHOLD_TITLE = "HTBW"
SUBENTRY_TYPE_ROOM = "room"
# Transient marker on a not-first #201 Room entry whose Room was already copied
# into the household entry; such an entry only removes itself.
CONF_MIGRATED_INTO = "migrated_into"

# Household/Integration-scoped settings (DL-145 SS2, placed by DL-148).
CONF_RETAIN_ENROLLMENT_RECORDINGS = "retain_enrollment_recordings"
RETENTION_RETAIN = "retain"
RETENTION_DELETE = "delete"

# Voice Evidence App connection, provisioned by Supervisor Discovery (#162 Choice A).
CONF_VOICE_EVIDENCE = "voice_evidence"
CONF_HOST = "host"
CONF_PORT = "port"
CONF_API_SECRET = "api_secret"
CONF_APP_SLUG = "app_slug"

# Voice Evidence App boundary (identity-contract.md, Contract A).
VOICE_EVIDENCE_CONTRACT_MAJOR = 1
VOICE_EVIDENCE_REQUEST_TIMEOUT_SECONDS = 10
VOICE_EVIDENCE_REFRESH_INTERVAL_SECONDS = 300
VOICE_EVIDENCE_UNREACHABLE_ISSUE_THRESHOLD = 3


class VoiceEvidenceOutcome(StrEnum):
    """Distinct DL-41 outcomes for the optional Voice Evidence App dependency.

    Each outcome names a different missing or failed dependency; none is an
    identity, trust, or permission failure, and none is ever emulated.
    """

    AVAILABLE = "available"
    NOT_CONFIGURED = "not_configured"
    UNREACHABLE = "unreachable"
    AUTHENTICATION_FAILED = "authentication_failed"
    INCOMPATIBLE = "incompatible"
    APP_UNAVAILABLE = "app_unavailable"


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
ISSUE_VOICE_EVIDENCE_PREFIX = "voice_evidence_"
ISSUE_MIGRATION_CONFLICT = "room_migration_conflict_{room_id}"

# External Storage Foundation (Issue #211, DL-151). Household/Integration-scoped
# (DL-148): the household supplies only the already-Home-Assistant-managed
# Share-usage path HTBW should use beneath, never NAS credentials.
CONF_EXTERNAL_STORAGE_PATH = "external_storage_path"
EXTERNAL_STORAGE_ROOT_NAME = "HTBW"
EXTERNAL_STORAGE_ROOT_MARKER = ".htbw-root.json"
EXTERNAL_STORAGE_ROOT_MARKER_VERSION = 1
EXTERNAL_STORAGE_HEALTH_PROBE_PREFIX = ".htbw-health-"
EXTERNAL_STORAGE_REFRESH_INTERVAL_SECONDS = 300
ISSUE_EXTERNAL_STORAGE_PREFIX = "external_storage_"
# A transient health check is reported only after it persists, exactly as
# Voice Evidence's own unreachable threshold (DL-41; never nag on one miss).
EXTERNAL_STORAGE_UNAVAILABLE_ISSUE_THRESHOLD = 3


class ExternalStorageOutcome(StrEnum):
    """Distinct DL-41 outcomes for the optional External Storage capability.

    Each outcome names a different missing or failed condition; none is an
    identity, trust, or permission failure, and none is ever emulated by a
    silent fallback to Home Assistant config storage, App `/data`, or another
    unmanaged location (DL-151 SS2.8).
    """

    AVAILABLE = "available"
    NOT_CONFIGURED = "not_configured"
    PATH_NOT_ALLOWED = "path_not_allowed"
    MEDIA_PATH_NOT_SUPPORTED = "media_path_not_supported"
    UNAVAILABLE = "unavailable"
    READ_ONLY = "read_only"
    WRITE_FAILED = "write_failed"
    INVALID_ROOT = "invalid_root"


# Single source of truth for "this is a standing, administrator-correctable
# failure" (consecutive-failure counting in ExternalStorageManager._set and
# Repairs issue eligibility in repairs_support.py both read this same set, so
# a new outcome added to one can never silently drift from the other).
EXTERNAL_STORAGE_FAILURE_OUTCOMES = frozenset(
    {
        ExternalStorageOutcome.PATH_NOT_ALLOWED,
        ExternalStorageOutcome.MEDIA_PATH_NOT_SUPPORTED,
        ExternalStorageOutcome.UNAVAILABLE,
        ExternalStorageOutcome.READ_ONLY,
        ExternalStorageOutcome.WRITE_FAILED,
        ExternalStorageOutcome.INVALID_ROOT,
    }
)
