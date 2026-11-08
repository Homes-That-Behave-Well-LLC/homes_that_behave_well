"""Governed Match Level vocabulary and the (uncalibrated) mapper interface.

Phase 2 defines no numeric thresholds. Calibration is a separately governed step; until
then every mapping attempt fails explicitly instead of guessing.
"""

from __future__ import annotations

from enum import Enum
from functools import total_ordering
from typing import Protocol


@total_ordering
class MatchLevel(Enum):
    NO_MATCH = "no_match"
    LOW = "low"
    MODERATE = "moderate"
    HIGH = "high"
    VERY_HIGH = "very_high"

    @property
    def rank(self) -> int:
        return _ORDER.index(self)

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, MatchLevel):
            return NotImplemented
        return self.rank < other.rank


_ORDER: tuple[MatchLevel, ...] = (
    MatchLevel.NO_MATCH,
    MatchLevel.LOW,
    MatchLevel.MODERATE,
    MatchLevel.HIGH,
    MatchLevel.VERY_HIGH,
)


class MatchLevelUncalibratedError(RuntimeError):
    """No governed calibration exists for the active compatibility identity."""

    reason_code = "uncalibrated"


class MatchLevelMapper(Protocol):
    """Maps an internal similarity value to an ordinal Match Level."""

    @property
    def calibrated(self) -> bool: ...

    def map(self, similarity: float) -> MatchLevel: ...


class UncalibratedMatchLevelMapper:
    """The only Phase 2 mapper: always reports that no calibration exists."""

    calibrated = False

    def map(self, similarity: float) -> MatchLevel:
        raise MatchLevelUncalibratedError("Match Level calibration is not available")
