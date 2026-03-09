"""Next-step MCP workflow simulation.

This demonstrates explicit protocol-like tool calls with structured payloads.
"""

from typing import Any, Dict, List

from adapters import MockTravelToolsAdapter, TravelToolsAdapter
from mcp_agent_init import MCPAgentRuntime
from models import TravelRequest, WorkflowResult
from tools import ToolExecutionError, ToolValidationError, execute_tool


class MCPWorkflowRunner:
    def __init__(
        self,
        runtime: MCPAgentRuntime,
        adapter: TravelToolsAdapter | None = None,
    ) -> None:
        self.runtime = runtime
        self.adapter = adapter or MockTravelToolsAdapter()

    def run_trip_planning(self, request: TravelRequest) -> WorkflowResult:
        steps: List[str] = []

        flight_payload: Dict[str, Any] = {
            "origin": request.origin,
            "destination": request.destination,
            "date": request.depart_date,
        }
        steps.append(f"MCP tool call -> search_flights {flight_payload}")
        try:
            flights = execute_tool("search_flights", flight_payload, self.adapter)
        except (ToolValidationError, ToolExecutionError) as exc:
            steps.append(f"MCP failure during flight lookup: {exc}")
            return WorkflowResult(
                architecture="MCP",
                summary="Trip planning halted due to a tool error.",
                steps=steps,
            )

        hotel_payload: Dict[str, Any] = {
            "city": request.destination,
            "check_in": request.depart_date,
            "check_out": request.return_date,
        }
        steps.append(f"MCP tool call -> search_hotels {hotel_payload}")
        try:
            hotels = execute_tool("search_hotels", hotel_payload, self.adapter)
        except (ToolValidationError, ToolExecutionError) as exc:
            steps.append(f"MCP failure during hotel lookup: {exc}")
            return WorkflowResult(
                architecture="MCP",
                summary="Trip planning halted due to a tool error.",
                steps=steps,
            )

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
