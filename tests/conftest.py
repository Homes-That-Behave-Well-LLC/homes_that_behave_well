"""Test-environment-only compatibility shim for running this suite natively on Windows.

pytest-homeassistant-custom-component's own `pytest_runtest_setup` hook calls
`pytest_socket.disable_socket(allow_unix_socket=True)` before every test, to
guarantee no test makes a real network connection. On Linux/macOS (where
Home Assistant's own CI runs this harness) that is sufficient, because
`socket.socketpair()` is a native syscall there and never touches
`socket.socket` at all.

Windows has no native `socketpair()`. CPython emulates it (see
`socket._fallback_socketpair` in the standard library) by opening a real
loopback TCP connection, which asyncio's own event-loop machinery
(`asyncio.proactor_events.BaseProactorEventLoop._make_self_pipe`) relies on
to build its internal wakeup self-pipe -- for every single event loop,
including the one pytest-asyncio's function-scoped `event_loop` fixture
creates per test. `pytest_socket.disable_socket()` replaces `socket.socket`
itself with a guarded class, so on Windows that internal, test-code-free
self-pipe construction is indistinguishable from a real test trying to open
a socket, and is blocked before a single line of test code runs.

This does not weaken the guard for anything a test itself does: only
`socket.socketpair()`'s own internal call is ever allowed through, and only
for the instant it needs to build asyncio's self-pipe. Every other socket
use -- in test code or in the integration under test -- is still blocked
exactly as pytest-homeassistant-custom-component intends.

This file exists only in this repository's local test environment; it does
not run as part of, or change anything about, the `htbw` integration
itself, and has no effect on Linux/macOS where the underlying problem does
not exist.
"""

import platform
import socket

if platform.system() == "Windows":
    _true_socket_class = socket.socket
    _real_socketpair = socket.socketpair

    def _unguarded_socketpair(
        *args: object, **kwargs: object
    ) -> tuple[socket.socket, socket.socket]:
        guarded_socket_class = socket.socket
        socket.socket = _true_socket_class
        try:
            return _real_socketpair(*args, **kwargs)  # type: ignore[arg-type]
        finally:
            socket.socket = guarded_socket_class

    socket.socketpair = _unguarded_socketpair
