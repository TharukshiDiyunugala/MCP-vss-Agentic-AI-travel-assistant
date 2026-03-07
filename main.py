"""Entry point that initializes and compares two travel assistant architectures."""

from pprint import pprint

from agentic_workflow import AgenticWorkflowRunner
from agentic_agent_init import AgenticTravelAgentInitializer
from mcp_workflow import MCPWorkflowRunner
from mcp_agent_init import MCPTravelAgentInitializer
from models import TravelRequest


def main() -> None:
    mcp_agent = MCPTravelAgentInitializer().initialize()
    agentic_agent = AgenticTravelAgentInitializer().initialize()
    request = TravelRequest(
        origin="Colombo",
        destination="Singapore",
        depart_date="2026-04-15",
        return_date="2026-04-20",
    )

    print("=== MCP Agent Initialization ===")
    pprint(mcp_agent.describe_architecture())

    print("\n=== Agentic AI Agent Initialization ===")
    pprint(agentic_agent.describe_architecture())

    mcp_result = MCPWorkflowRunner(mcp_agent).run_trip_planning(request)
    agentic_result = AgenticWorkflowRunner(agentic_agent).run_trip_planning(request)

    print("\n=== Next Step: MCP Workflow Run ===")
    pprint(mcp_result)

    print("\n=== Next Step: Agentic Workflow Run ===")
    pprint(agentic_result)


if __name__ == "__main__":
    main()
