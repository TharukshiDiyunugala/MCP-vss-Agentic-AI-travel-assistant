"""Tool adapter interfaces and mock provider implementations.

This keeps execution logic separate from orchestration so providers can be
swapped later (real API, sandbox, test doubles).
"""

from dataclasses import dataclass
from typing import Any, Dict, Protocol


class TravelToolsAdapter(Protocol):
    def search_flights(self, origin: str, destination: str, date: str) -> list[Dict[str, Any]]:
        ...

    def search_hotels(self, city: str, check_in: str, check_out: str) -> list[Dict[str, Any]]:
        ...


@dataclass
class MockTravelToolsAdapter:
    """Default adapter used by the demo until real APIs are connected."""

    def search_flights(self, origin: str, destination: str, date: str) -> list[Dict[str, Any]]:
        return [
            {
                "flight_id": "FL-102",
                "origin": origin,
                "destination": destination,
                "date": date,
                "price_usd": 420,
                "provider": "mock-provider",
            }
        ]

    def search_hotels(self, city: str, check_in: str, check_out: str) -> list[Dict[str, Any]]:
        return [
            {
                "hotel_id": "HT-77",
                "city": city,
                "check_in": check_in,
                "check_out": check_out,
                "nightly_usd": 150,
                "provider": "mock-provider",
            }
        ]
