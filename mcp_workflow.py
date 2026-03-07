"""Next-step MCP workflow simulation.

This demonstrates explicit protocol-like tool calls with structured payloads.
"""

from typing import Any, Dict, List

from mcp_agent_init import MCPAgentRuntime
from models import TravelRequest, WorkflowResult
from tools import execute_tool


class MCPWorkflowRunner:
    def __init__(self, runtime: MCPAgentRuntime) -> None:
        self.runtime = runtime

    def run_trip_planning(self, request: TravelRequest) -> WorkflowResult:
        steps: List[str] = []

        flight_payload: Dict[str, Any] = {
            "origin": request.origin,
            "destination": request.destination,
            "date": request.depart_date,
        }
        steps.append(f"MCP tool call -> search_flights {flight_payload}")
        flights = execute_tool("search_flights", flight_payload)

        hotel_payload: Dict[str, Any] = {
            "city": request.destination,
            "check_in": request.depart_date,
            "check_out": request.return_date,
        }
        steps.append(f"MCP tool call -> search_hotels {hotel_payload}")
        hotels = execute_tool("search_hotels", hotel_payload)

        steps.append("MCP response synthesis from structured tool outputs")
        summary = (
            f"Selected 1 flight option and 1 hotel option for {request.destination}. "
            f"(flight={flights[0]['flight_id']}, hotel={hotels[0]['hotel_id']})"
        )

        return WorkflowResult(
            architecture="MCP",
            summary=summary,
            steps=steps,
        )
