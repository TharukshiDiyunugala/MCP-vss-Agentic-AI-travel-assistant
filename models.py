"""Shared request/response models for demo workflows."""

from dataclasses import dataclass


@dataclass(frozen=True)
class TravelRequest:
    origin: str
    destination: str
    depart_date: str
    return_date: str


@dataclass(frozen=True)
class WorkflowResult:
    architecture: str
    summary: str
    steps: list[str]
