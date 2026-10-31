from typing import Dict, Any, List, Optional
from pydantic import BaseModel

class DomainExecutionResult(BaseModel):
    success: bool
    status_code: str
    message: str
    data: Dict[str, Any]

class ConseilCavisteEngine:
    """Moteur métier déterministe pour le domaine 'conseil_caviste'."""
    def __init__(self, engine_config: Optional[Dict[str, Any]] = None):
        self.config = engine_config or {
        "domain_type": "conseil_caviste",
        "action_on_complete": "synthesize_and_deliver"
}

    def validate_facts(self, facts: Dict[str, Any]) -> List[str]:
        errors = []
        if "montant" in facts and float(facts["montant"]) < 0:
            errors.append("Le montant ne peut pas être négatif.")
        return errors

    def execute(self, session_id: str, confirmed_facts: Dict[str, Any]) -> DomainExecutionResult:
        errors = self.validate_facts(confirmed_facts)
        if errors:
            return DomainExecutionResult(success=False, status_code="VALIDATION_FAILED", message="; ".join(errors), data={"errors": errors})

        return DomainExecutionResult(
            success=True,
            status_code="EXECUTION_CONFIRMED",
            message="Opération métier exécutée avec succès.",
            data={"session_id": session_id, "domain_type": "conseil_caviste", "processed_facts": confirmed_facts, "confirmation_reference": f"REF-{session_id[:8].upper()}"}
        )
