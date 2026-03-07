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


def search_flights(origin: str, destination: str, date: str) -> list[Dict[str, Any]]:
    """Mock flight search used for architecture demonstrations."""
    return [
        {
            "flight_id": "FL-102",
            "origin": origin,
            "destination": destination,
            "date": date,
            "price_usd": 420,
        }
    ]


def search_hotels(city: str, check_in: str, check_out: str) -> list[Dict[str, Any]]:
    """Mock hotel search used for architecture demonstrations."""
    return [
        {
            "hotel_id": "HT-77",
            "city": city,
            "check_in": check_in,
            "check_out": check_out,
            "nightly_usd": 150,
        }
    ]


def execute_tool(tool_name: str, payload: Dict[str, Any]) -> list[Dict[str, Any]]:
    """Dispatch demo tool calls by name."""
    if tool_name == "search_flights":
        return search_flights(**payload)
    if tool_name == "search_hotels":
        return search_hotels(**payload)
    raise ValueError(f"Unsupported tool: {tool_name}")
