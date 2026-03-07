"""Initialization model for an Agentic AI travel assistant.

Agentic architecture emphasis:
- Internal planner + memory + executor loop.
- Goal decomposition into subtasks.
- Iterative reasoning until completion criteria are met.
"""

from dataclasses import dataclass
from typing import Any, Dict, List

from tools import TOOL_SPECS


@dataclass
class AgenticLoopConfig:
    planner: str
    max_iterations: int
    stop_condition: str


@dataclass
class AgenticAgentRuntime:
    agent_name: str
    loop_config: AgenticLoopConfig
    tools: List[str]
    memory: Dict[str, Any]
    workflow_stages: List[str]

    def describe_architecture(self) -> Dict[str, Any]:
        return {
            "agent": self.agent_name,
            "architecture": "Agentic AI",
            "tool_integration": "Tools invoked by internal planner/executor decisions",
            "reasoning_workflow": "Observe -> Plan -> Act -> Reflect loop",
            "task_pattern": "Goal -> Subtasks -> Tool Actions -> Final Itinerary",
            "tool_count": len(self.tools),
            "max_iterations": self.loop_config.max_iterations,
        }


class AgenticTravelAgentInitializer:
    def __init__(self, agent_name: str = "AgenticTravelAssistant") -> None:
        self.agent_name = agent_name

    def initialize(self) -> AgenticAgentRuntime:
        loop_config = AgenticLoopConfig(
            planner="hierarchical-task-planner",
            max_iterations=6,
            stop_condition="itinerary_confidence>=0.9 OR user_approved",
        )
        memory = {
            "short_term": [],
            "long_term_profile": {
                "seat_preference": "aisle",
                "hotel_style": "business",
            },
        }
        workflow_stages = [
            "intent_capture",
            "constraint_extraction",
            "subtask_planning",
            "tool_execution",
            "self_reflection",
            "response_synthesis",
        ]
        tool_names = [spec.name for spec in TOOL_SPECS]

        return AgenticAgentRuntime(
            agent_name=self.agent_name,
            loop_config=loop_config,
            tools=tool_names,
            memory=memory,
            workflow_stages=workflow_stages,
        )
