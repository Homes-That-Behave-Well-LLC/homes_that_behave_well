"""Home Assistant App packaging: config.yaml, translations, repository manifest."""

from __future__ import annotations

from pathlib import Path

import yaml

from htbw_voice_evidence.const import APP_VERSION, DEFAULT_PORT, DISCOVERY_SERVICE

APP_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = APP_DIR.parents[1]


def load(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def test_config_yaml_follows_owner_decisions() -> None:
    config = load(APP_DIR / "config.yaml")
    assert config["slug"] == "htbw_voice_evidence"
    assert config["version"] == APP_VERSION == "0.1.0"
    assert set(config["arch"]) == {"amd64", "aarch64"}
    assert config["discovery"] == [DISCOVERY_SERVICE]
    assert config["stdin"] is True
    assert config["init"] is False
    assert config["options"] == {"retain_enrollment_recordings": False}
    assert config["schema"] == {"retain_enrollment_recordings": "bool"}
    assert config["watchdog"] == f"tcp://[HOST]:[PORT:{DEFAULT_PORT}]"
    for forbidden in (
        "ports",
        "homeassistant_api",
        "hassio_api",
        "hassio_role",
        "auth_api",
        "host_network",
        "privileged",
        "full_access",
        "docker_api",
        "map",
        "ingress",
    ):
        assert forbidden not in config


def test_translation_states_htbw_management() -> None:
    translation = load(APP_DIR / "translations" / "en.yaml")
    description = translation["configuration"]["retain_enrollment_recordings"]["description"]
    assert (
        "Managed by HTBW — set in HTBW Household configuration; changes here are overwritten."
        in " ".join(description.split())
    )


def test_repository_manifest() -> None:
    manifest = load(REPO_ROOT / "repository.yaml")
    assert manifest["name"]


def test_dockerfile_uses_pinned_debian_base() -> None:
    dockerfile = (APP_DIR / "Dockerfile").read_text(encoding="utf-8")
    from_lines = [line for line in dockerfile.splitlines() if line.startswith("FROM ")]
    assert from_lines == ["FROM ghcr.io/home-assistant/base-debian:trixie-2026.11.0"]
    assert "python3 python3-venv" in dockerfile


def test_no_model_binary_in_app_tree() -> None:
    assert not list(APP_DIR.rglob("*.onnx"))
