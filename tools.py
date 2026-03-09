"""Shared travel tools used by both architectures.

These are intentionally simple placeholders so the project focuses on
initialization architecture, not full business logic.
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict

from adapters import MockTravelToolsAdapter, TravelToolsAdapter


@dataclass(frozen=True)
class ToolSpec:
    name: str
    description: str
    input_schema: Dict[str, Any]


SEARCH_FLIGHTS = ToolSpec(
    name="search_flights",
    description="Find flights between two cities for a travel date.",
    input_schema={
        "type": "object",
        "properties": {
            "origin": {"type": "string"},
            "destination": {"type": "string"},
            "date": {"type": "string", "format": "date"},
        },
        "required": ["origin", "destination", "date"],
    },
)

SEARCH_HOTELS = ToolSpec(
    name="search_hotels",
    description="Find hotels in a city for check-in/check-out dates.",
    input_schema={
        "type": "object",
        "properties": {
            "city": {"type": "string"},
            "check_in": {"type": "string", "format": "date"},
            "check_out": {"type": "string", "format": "date"},
        },
        "required": ["city", "check_in", "check_out"],
    },
)

TOOL_SPECS = [SEARCH_FLIGHTS, SEARCH_HOTELS]
TOOL_SPEC_BY_NAME = {spec.name: spec for spec in TOOL_SPECS}


class ToolValidationError(ValueError):
    """Raised when a tool payload fails schema validation."""


class ToolExecutionError(RuntimeError):
    """Raised when tool execution fails."""


def _validate_date(date_value: str, field_name: str) -> None:
    try:
        datetime.strptime(date_value, "%Y-%m-%d")
    except ValueError as exc:
        raise ToolValidationError(f"{field_name} must be YYYY-MM-DD") from exc


def validate_tool_payload(tool_name: str, payload: Dict[str, Any]) -> None:
    spec = TOOL_SPEC_BY_NAME.get(tool_name)
    if spec is None:
        raise ToolValidationError(f"Unsupported tool: {tool_name}")

    required = spec.input_schema.get("required", [])
    for field in required:
        if field not in payload:
            raise ToolValidationError(f"Missing required field '{field}' for {tool_name}")

    properties = spec.input_schema.get("properties", {})
    for field_name, definition in properties.items():
        if field_name not in payload:
            continue
        value = payload[field_name]
        expected_type = definition.get("type")
        if expected_type == "string" and not isinstance(value, str):
            raise ToolValidationError(f"{field_name} must be a string for {tool_name}")
        if definition.get("format") == "date":
            _validate_date(value, field_name)


def execute_tool(
    tool_name: str,
    payload: Dict[str, Any],
    adapter: TravelToolsAdapter | None = None,
) -> list[Dict[str, Any]]:
    """Validate and dispatch tool calls through a pluggable adapter."""
    validate_tool_payload(tool_name, payload)
    runtime_adapter = adapter or MockTravelToolsAdapter()

    try:
        if tool_name == "search_flights":
            return runtime_adapter.search_flights(**payload)
        if tool_name == "search_hotels":
            return runtime_adapter.search_hotels(**payload)
    except Exception as exc:  # pragma: no cover - defensive for future providers
        raise ToolExecutionError(f"Tool '{tool_name}' failed: {exc}") from exc

    raise ToolValidationError(f"Unsupported tool: {tool_name}")
