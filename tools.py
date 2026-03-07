"""Shared travel tools used by both architectures.

These are intentionally simple placeholders so the project focuses on
initialization architecture, not full business logic.
"""

from dataclasses import dataclass
from typing import Any, Dict


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
