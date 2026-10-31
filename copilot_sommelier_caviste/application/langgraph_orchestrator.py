from typing import Dict, Any, TypedDict

class AgentState(TypedDict):
    session_id: str
    user_input: str
    confirmed_facts: Dict[str, Any]
    next_question: str
    is_completed: bool

class LangGraphOrchestrator:
    """Extension d'orchestration pour LangGraph / StateGraph."""
    def run_turn(self, state: AgentState) -> AgentState:
        return state
