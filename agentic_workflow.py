"""Next-step Agentic workflow simulation.

This demonstrates a simple Observe -> Plan -> Act -> Reflect loop.
"""

from typing import List

from adapters import MockTravelToolsAdapter, TravelToolsAdapter
from agentic_agent_init import AgenticAgentRuntime
from models import TravelRequest, WorkflowResult
from tools import ToolExecutionError, ToolValidationError, execute_tool


class AgenticWorkflowRunner:
    def __init__(
        self,
        runtime: AgenticAgentRuntime,
        adapter: TravelToolsAdapter | None = None,
    ) -> None:
        self.runtime = runtime
        self.adapter = adapter or MockTravelToolsAdapter()

    def run_trip_planning(self, request: TravelRequest) -> WorkflowResult:
        steps: List[str] = []

        steps.append("Observe: parse user intent and constraints")
        subtasks = [
            "find best outbound flight",
            "find central hotel near business district",
            "merge into draft itinerary",
        ]
        steps.append(f"Plan: generated subtasks {subtasks}")

        try:
            flights = execute_tool(
                "search_flights",
                {
                    "origin": request.origin,
                    "destination": request.destination,
                    "date": request.depart_date,
                },
                self.adapter,
            )
        except (ToolValidationError, ToolExecutionError) as exc:
            steps.append(f"Act failed (flights): {exc}")
            return WorkflowResult(
                architecture="Agentic AI",
                summary="Agent loop stopped due to a tool failure.",
                steps=steps,
            )
        steps.append("Act: searched flights")

        try:
            hotels = execute_tool(
                "search_hotels",
                {
                    "city": request.destination,
                    "check_in": request.depart_date,
                    "check_out": request.return_date,
                },
                self.adapter,
            )
        except (ToolValidationError, ToolExecutionError) as exc:
            steps.append(f"Act failed (hotels): {exc}")
            return WorkflowResult(
                architecture="Agentic AI",
                summary="Agent loop stopped due to a tool failure.",
                steps=steps,
            )
        steps.append("Act: searched hotels")

        steps.append("Reflect: confidence improved after tool evidence")
        summary = (
            f"Draft itinerary ready for {request.destination}. "
            f"Top picks: {flights[0]['flight_id']} + {hotels[0]['hotel_id']}"
        )

        return WorkflowResult(
            architecture="Agentic AI",
            summary=summary,
            steps=steps,
        )
