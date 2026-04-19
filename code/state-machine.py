#!/usr/bin/env python3
"""Agent expressed as an explicit state machine (not a single prompt loop)."""
from dataclasses import dataclass, field
from typing import Any, Callable

@dataclass
class AgentState:
    turn: int = 0
    goal: str = ""
    scratchpad: list[dict] = field(default_factory=list)
    last_action: str = ""
    last_result: Any = None
    retries: int = 0
    max_retries: int = 3

def plan(s: AgentState, llm: Callable) -> str:
    return llm(f"goal={s.goal}\nscratchpad={s.scratchpad}\nchoose next action")

def act(s: AgentState, action: str, tools: dict) -> Any:
    if action not in tools:
        raise KeyError(action)
    return tools[action]()

def step(s: AgentState, llm, tools) -> tuple[AgentState, str]:
    if s.retries >= s.max_retries:
        return s, "FAILED"
    s.turn += 1
    action = plan(s, llm)
    s.last_action = action
    try:
        s.last_result = act(s, action, tools)
        s.scratchpad.append({"action": action, "result": str(s.last_result)[:200]})
        s.retries = 0
    except Exception as e:
        s.retries += 1
        s.scratchpad.append({"action": action, "error": str(e)})
        return s, "RETRY"
    # separate review step decides termination
    done = llm(f"scratchpad={s.scratchpad}\ngoal met? yes|no|more").strip().lower()
    if done.startswith("yes"):
        return s, "DONE"
    return s, "CONTINUE"
