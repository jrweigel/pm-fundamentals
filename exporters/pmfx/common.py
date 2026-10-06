from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import yaml


TOKEN = re.compile(r"\{\{\s*([A-Za-z0-9_.-]+)\s*\}\}")


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as stream:
        value = yaml.safe_load(stream) or {}
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a YAML mapping")
    return value


def flatten(value: Any, prefix: str = "") -> dict[str, str]:
    result: dict[str, str] = {}
    if isinstance(value, dict):
        for key, child in value.items():
            result.update(flatten(child, f"{prefix}.{key}" if prefix else str(key)))
    elif isinstance(value, list):
        result[prefix] = ", ".join(str(item) for item in value)
    else:
        result[prefix] = "" if value is None else str(value)
    return result


def render(text: str, values: dict[str, Any]) -> str:
    flattened = flatten(values)

    def replace(match: re.Match[str]) -> str:
        return flattened.get(match.group(1), str(values.get(match.group(1), match.group(0))))

    return TOKEN.sub(replace, text)


def project_values(project_dir: Path) -> dict[str, Any]:
    values = load_yaml(project_dir / "project.yaml")
    for filename in ("plan.yaml", "raid.yaml", "decisions.yaml", "evidence.yaml"):
        path = project_dir / filename
        if path.exists():
            values[Path(filename).stem] = load_yaml(path)
    return values
