"""Minimal Supervisor API client (discovery and own options) with bounded timeouts."""

from __future__ import annotations

import re
from typing import Any

import aiohttp

from .const import SUPERVISOR_TIMEOUT_S

_UUID_RE = re.compile(r"[0-9A-Fa-f-]{1,64}")


class SupervisorError(Exception):
    """A Supervisor API call failed. Messages never contain request bodies."""


class SupervisorClient:
    def __init__(
        self,
        base_url: str,
        token: str,
        timeout_s: float = SUPERVISOR_TIMEOUT_S,
        session: aiohttp.ClientSession | None = None,
    ) -> None:
        self._base_url = base_url.rstrip("/")
        self._token = token
        self._timeout = aiohttp.ClientTimeout(total=timeout_s)
        self._session = session
        self._owns_session = session is None

    async def _get_session(self) -> aiohttp.ClientSession:
        if self._session is None or self._session.closed:
            self._session = aiohttp.ClientSession(timeout=self._timeout)
            self._owns_session = True
        return self._session

    async def close(self) -> None:
        if self._owns_session and self._session is not None and not self._session.closed:
            await self._session.close()

    async def _request(
        self, method: str, path: str, payload: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        session = await self._get_session()
        headers = {"Authorization": f"Bearer {self._token}"}
        try:
            async with session.request(
                method,
                f"{self._base_url}{path}",
                json=payload,
                headers=headers,
                timeout=self._timeout,
            ) as resp:
                if resp.status >= 400:
                    raise SupervisorError(f"{method} {path} returned HTTP {resp.status}")
                if resp.content_type != "application/json":
                    return {}
                body = await resp.json()
        except (aiohttp.ClientError, TimeoutError, ValueError) as err:
            raise SupervisorError(f"{method} {path} failed: {type(err).__name__}") from err
        if not isinstance(body, dict):
            raise SupervisorError(f"{method} {path} returned an unexpected body")
        if body.get("result") not in (None, "ok"):
            raise SupervisorError(f"{method} {path} returned result={body.get('result')}")
        data = body.get("data")
        return data if isinstance(data, dict) else {}

    async def post_discovery(self, service: str, config: dict[str, Any]) -> str:
        data = await self._request("POST", "/discovery", {"service": service, "config": config})
        uuid = data.get("uuid")
        if not isinstance(uuid, str) or not uuid:
            raise SupervisorError("POST /discovery returned no uuid")
        return uuid

    async def delete_discovery(self, uuid: str) -> None:
        if not _UUID_RE.fullmatch(uuid):
            raise SupervisorError("invalid discovery uuid")
        await self._request("DELETE", f"/discovery/{uuid}")

    async def get_own_options(self) -> dict[str, Any]:
        data = await self._request("GET", "/addons/self/info")
        options = data.get("options")
        if not isinstance(options, dict):
            raise SupervisorError("GET /addons/self/info returned no options")
        return options
