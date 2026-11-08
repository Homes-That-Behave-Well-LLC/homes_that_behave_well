"""Dual-distribution conformance: Marketplace integration and Home Assistant App.

The repository ships two independent runtimes through two official channels:

- `custom_components/htbw` through the Home Assistant Marketplace (`hacs.json`);
- `apps/htbw_voice_evidence` through the Supervisor app store (`repository.yaml`).

These checks encode the layout rules each channel applies, so a change that would
break either channel, or let one channel's metadata interfere with the other, fails
here before it reaches users. The rules mirror the official sources recorded in
docs/governance/home-assistant-quality.md:

- Marketplace integration resolution (core 2026.11.0,
  homeassistant/components/marketplace/repositories/integration.py): it installs the
  first folder under `custom_components/`; it refuses a repository as an app
  repository only when no such folder exists and a `repository.yaml` does.
- Marketplace `hacs.json` keys (utils/validate.py, REPOSITORY_MANIFEST_VALUES).
- Supervisor app discovery: any `config.yaml|yml|json` at any depth, skipping hidden
  folders and folders named `rootfs`.
"""

from __future__ import annotations

import json
import re
import struct
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
INTEGRATION = ROOT / "custom_components" / "htbw"
APP = ROOT / "apps" / "htbw_voice_evidence"

HACS_KEYS: dict[str, type | tuple[type, ...]] = {
    "name": str,
    "content_in_root": bool,
    "filename": str,
    "zip_release": bool,
    "persistent_directory": str,
    "homeassistant": str,
    "hide_default_branch": bool,
    "hacs": str,
    "country": (str, list),
}
APP_CONFIG_NAMES = {"config.yaml", "config.yml", "config.json"}
REPOSITORY_NAMES = {"repository.yaml", "repository.yml", "repository.json"}
SKIPPED_DIRS = {".git", ".venv", "node_modules", "__pycache__"}


def _json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _yaml(path: Path) -> Any:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _png_size(path: Path) -> tuple[int, int]:
    header = path.read_bytes()[:24]
    assert header[:8] == b"\x89PNG\r\n\x1a\n", f"{path.name} is not a PNG"
    width, height = struct.unpack(">II", header[16:24])
    return width, height


def _version_tuple(value: str) -> tuple[int, ...]:
    return tuple(int(part) for part in re.findall(r"\d+", value)[:3])


def _supervisor_app_configs() -> list[Path]:
    """Return every file the Supervisor would read as an app configuration."""
    found: list[Path] = []
    for path in ROOT.rglob("*"):
        relative = path.relative_to(ROOT)
        if any(
            part.startswith(".") or part == "rootfs" or part in SKIPPED_DIRS
            for part in relative.parts[:-1]
        ):
            continue
        if path.is_file() and path.name in APP_CONFIG_NAMES:
            found.append(relative)
    return found


# --- Marketplace: custom integration ---------------------------------------


def test_hacs_json_uses_only_marketplace_keys_with_valid_types() -> None:
    hacs = _json(ROOT / "hacs.json")
    assert set(hacs) <= set(HACS_KEYS), set(hacs) - set(HACS_KEYS)
    for key, value in hacs.items():
        assert isinstance(value, HACS_KEYS[key]), key
    assert "content_in_root" not in hacs
    assert "zip_release" not in hacs


def test_hacs_name_matches_manifest_name() -> None:
    assert _json(ROOT / "hacs.json")["name"] == _json(INTEGRATION / "manifest.json")["name"]


def test_minimum_home_assistant_matches_tested_core() -> None:
    minimum = _json(ROOT / "hacs.json")["homeassistant"]
    pinned = re.search(
        r"^homeassistant==(\S+)$",
        (ROOT / "requirements-dev.txt").read_text(encoding="utf-8"),
        re.M,
    )
    assert pinned is not None
    assert _version_tuple(minimum) <= _version_tuple(pinned.group(1))


def test_marketplace_resolves_exactly_one_integration_folder() -> None:
    folders = [p for p in (ROOT / "custom_components").iterdir() if p.is_dir()]
    folders = [p for p in folders if p.name not in SKIPPED_DIRS]
    assert [p.name for p in folders] == ["htbw"]
    # The Marketplace treats repository.yaml as an app repository only when this folder
    # is missing; with it present the integration resolves normally.
    assert (ROOT / "custom_components" / "htbw" / "manifest.json").is_file()


def test_manifest_has_every_key_marketplace_and_hacs_require() -> None:
    manifest = _json(INTEGRATION / "manifest.json")
    assert manifest["domain"] == INTEGRATION.name
    assert re.fullmatch(r"[a-z0-9_-]+", manifest["domain"])
    assert re.fullmatch(r"\d+\.\d+\.\d+", manifest["version"])
    repository = "https://github.com/Homes-That-Behave-Well-LLC/homes_that_behave_well"
    assert manifest["documentation"].startswith(repository)
    assert manifest["issue_tracker"] == f"{repository}/issues"
    assert manifest["codeowners"]
    assert manifest["config_flow"] is True
    assert "quality_scale" not in manifest


def test_brand_icons_ship_inside_the_integration() -> None:
    brand = INTEGRATION / "brand"
    assert _png_size(brand / "icon.png") == (256, 256)
    assert _png_size(brand / "icon@2x.png") == (512, 512)
    assert _png_size(brand / "dark_icon.png") == (256, 256)
    assert _png_size(brand / "dark_icon@2x.png") == (512, 512)


def test_shipped_english_translation_matches_strings() -> None:
    assert _json(INTEGRATION / "translations" / "en.json") == _json(INTEGRATION / "strings.json")


def test_integration_download_holds_no_app_or_development_artifacts() -> None:
    for path in INTEGRATION.rglob("*"):
        if "__pycache__" in path.parts or path.is_dir():
            continue
        assert path.suffix in {".py", ".json", ".png"}, path.relative_to(ROOT)
        assert path.name not in APP_CONFIG_NAMES | REPOSITORY_NAMES


# --- App store: Home Assistant App ------------------------------------------


def test_repository_yaml_is_valid_for_the_supervisor() -> None:
    repository = _yaml(ROOT / "repository.yaml")
    assert isinstance(repository.get("name"), str) and repository["name"]
    assert repository["url"] == (
        "https://github.com/Homes-That-Behave-Well-LLC/homes_that_behave_well"
    )


def test_supervisor_discovers_exactly_the_voice_evidence_app() -> None:
    assert _supervisor_app_configs() == [Path("apps/htbw_voice_evidence/config.yaml")]


def test_app_config_is_consistent_with_its_folder_changelog_and_integration() -> None:
    config = _yaml(APP / "config.yaml")
    assert config["slug"] == APP.name
    assert re.fullmatch(r"\d+\.\d+\.\d+", config["version"])
    first_heading = re.search(
        r"^## (\S+)", (APP / "CHANGELOG.md").read_text(encoding="utf-8"), re.M
    )
    assert first_heading is not None and first_heading.group(1) == config["version"]
    assert set(config["arch"]) <= {"amd64", "aarch64"}
    assert config["discovery"] == [_json(INTEGRATION / "manifest.json")["domain"]]
    assert "ports" not in config
    assert "image" not in config, "prebuilt image publication is an Owner release decision"
    for name in ("Dockerfile", "README.md", "DOCS.md", "translations/en.yaml"):
        assert (APP / name).is_file(), name
