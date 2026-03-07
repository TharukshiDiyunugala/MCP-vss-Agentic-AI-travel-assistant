"""Initialization model for an MCP-style travel assistant.

MCP architecture emphasis:
- Externalized tools with explicit schemas.
- Protocol-level server/session handshake.
- Stateless tool calls coordinated through context.
"""

from dataclasses import dataclass
from typing import Any, Dict, List

from tools import TOOL_SPECS


@dataclass
class MCPServerConfig:
    server_name: str
    transport: str
    endpoint: str


@dataclass
class MCPAgentRuntime:
    agent_name: str
    server: MCPServerConfig
    tool_registry: Dict[str, Dict[str, Any]]
    session_context: Dict[str, Any]

    def describe_architecture(self) -> Dict[str, Any]:
        return {
            "agent": self.agent_name,
            "architecture": "Model Context Protocol (MCP)",
            "tool_integration": "External tools exposed via MCP server + JSON schemas",
            "reasoning_workflow": "Model delegates actions as protocol tool calls",
            "task_pattern": "Request -> Context -> Tool Call -> Structured Response",
            "tool_count": len(self.tool_registry),
            "server_endpoint": self.server.endpoint,
        }


class MCPTravelAgentInitializer:
    def __init__(self, agent_name: str = "MCPTravelAssistant") -> None:
        self.agent_name = agent_name

    def initialize(self) -> MCPAgentRuntime:
        tool_registry = {spec.name: spec.input_schema for spec in TOOL_SPECS}
        server = MCPServerConfig(
            server_name="travel-tools-mcp-server",
            transport="stdio",
            endpoint="mcp://travel-tools",
        )
        session_context = {
            "domain": "travel",
            "response_format": "json",
            "safety_policy": "booking-read-only",
        }

        return MCPAgentRuntime(
            agent_name=self.agent_name,
            server=server,
            tool_registry=tool_registry,
            session_context=session_context,
        )
