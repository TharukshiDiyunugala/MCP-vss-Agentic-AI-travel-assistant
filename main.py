"""Entry point that initializes and compares two travel assistant architectures."""

from pprint import pprint

from agentic_agent_init import AgenticTravelAgentInitializer
from mcp_agent_init import MCPTravelAgentInitializer


def main() -> None:
    mcp_agent = MCPTravelAgentInitializer().initialize()
    agentic_agent = AgenticTravelAgentInitializer().initialize()

    print("=== MCP Agent Initialization ===")
    pprint(mcp_agent.describe_architecture())

    print("\n=== Agentic AI Agent Initialization ===")
    pprint(agentic_agent.describe_architecture())


if __name__ == "__main__":
    main()
