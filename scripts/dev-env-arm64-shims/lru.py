"""Minimal pure-Python shim for the ``lru-dict`` C extension (module ``lru``).

Installed only by scripts/setup-dev-env.ps1's ARM64 Windows compatibility
layer, into the repository-local .venv's site-packages -- never shipped as
part of the HTBW Core integration itself (manifest.json declares no
requirements) and never used by the actual Home Assistant deployment target.

No prebuilt ``lru-dict`` wheel is available for win_arm64 at any released
version, and this development machine has no C toolchain to build one from
source. Home Assistant's ``helpers.template`` module (and a few components
not exercised by this integration's tests) use ``lru.LRU`` purely as a
size-bounded, order-aware cache dict. This shim reproduces that subset of
the real extension's API using ``collections.OrderedDict``.
"""

from __future__ import annotations

from collections import OrderedDict
from typing import Any, Callable, Generic, Iterator, TypeVar

_K = TypeVar("_K")
_V = TypeVar("_V")

_MISSING = object()


class LRU(Generic[_K, _V]):
    """A minimal least-recently-used cache dict, API-compatible with lru-dict."""

    def __init__(self, size: int, callback: Callable[[_K, _V], None] | None = None) -> None:
        if size < 1:
            raise ValueError("Size must be a positive number")
        self._size = size
        self._callback = callback
        self._data: OrderedDict[_K, _V] = OrderedDict()

    def __class_getitem__(cls, item: Any) -> Any:
        return cls

    def __setitem__(self, key: _K, value: _V) -> None:
        if key in self._data:
            self._data.move_to_end(key)
        self._data[key] = value
        while len(self._data) > self._size:
            evicted_key, evicted_value = self._data.popitem(last=False)
            if self._callback is not None:
                self._callback(evicted_key, evicted_value)

    def __getitem__(self, key: _K) -> _V:
        value = self._data[key]
        self._data.move_to_end(key)
        return value

    def __delitem__(self, key: _K) -> None:
        del self._data[key]

    def __contains__(self, key: object) -> bool:
        return key in self._data

    def __len__(self) -> int:
        return len(self._data)

    def __iter__(self) -> Iterator[_K]:
        return iter(self._data)

    def get(self, key: _K, default: Any = None) -> Any:
        value = self._data.get(key, _MISSING)
        if value is _MISSING:
            return default
        self._data.move_to_end(key)
        return value

    def keys(self) -> Any:
        return self._data.keys()

    def values(self) -> Any:
        return self._data.values()

    def items(self) -> Any:
        return self._data.items()

    def peek_first_item(self) -> tuple[_K, _V] | None:
        if not self._data:
            return None
        key = next(iter(self._data))
        return key, self._data[key]

    def set_callback(self, callback: Callable[[_K, _V], None] | None) -> None:
        self._callback = callback

    def clear(self) -> None:
        self._data.clear()

    def get_size(self) -> int:
        return self._size

    def set_size(self, size: int) -> None:
        if size < 1:
            raise ValueError("Size must be a positive number")
        self._size = size
        while len(self._data) > self._size:
            evicted_key, evicted_value = self._data.popitem(last=False)
            if self._callback is not None:
                self._callback(evicted_key, evicted_value)

    has_key = __contains__
