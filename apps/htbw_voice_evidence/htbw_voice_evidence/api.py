"""Contract A HTTP API (aiohttp). Every route requires the App bearer secret."""

from __future__ import annotations

from collections.abc import Awaitable, Callable
from typing import TYPE_CHECKING

from aiohttp import web

if TYPE_CHECKING:
    from .runtime import EvidenceRuntime

RUNTIME_KEY: web.AppKey[EvidenceRuntime] = web.AppKey("runtime")
_BEARER_PREFIX = "Bearer "
_UNAUTHORIZED_BODY = {"error": "unauthorized"}

Handler = Callable[[web.Request], Awaitable[web.StreamResponse]]


def _unauthorized() -> web.Response:
    return web.json_response(_UNAUTHORIZED_BODY, status=401, headers={"WWW-Authenticate": "Bearer"})


@web.middleware
async def auth_middleware(request: web.Request, handler: Handler) -> web.StreamResponse:
    runtime = request.app[RUNTIME_KEY]
    header = request.headers.get("Authorization", "")
    token = header[len(_BEARER_PREFIX) :] if header.startswith(_BEARER_PREFIX) else None
    if not runtime.secrets.verify(token):
        return _unauthorized()
    try:
        return await handler(request)
    except web.HTTPException as exc:
        return web.json_response(
            {"error": "not_found" if exc.status == 404 else "error"}, status=exc.status
        )


async def handle_status(request: web.Request) -> web.Response:
    return web.json_response(request.app[RUNTIME_KEY].status_payload())


async def handle_health(request: web.Request) -> web.Response:
    return web.json_response(request.app[RUNTIME_KEY].health_payload())


def create_app(runtime: EvidenceRuntime) -> web.Application:
    app = web.Application(middlewares=[auth_middleware], client_max_size=64 * 1024)
    app[RUNTIME_KEY] = runtime
    app.router.add_get("/v1/status", handle_status)
    app.router.add_get("/v1/health", handle_health)
    return app
