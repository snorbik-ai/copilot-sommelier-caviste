from typing import Dict, Any, List
from datetime import datetime

class ContextPipelineBuilder:
    """Générateur déterministe du prompt système LLM en 7 sections inviolables."""
    def __init__(self, agent_name: str = "Copilot Sommelier & Accords Vins", role: str = "Conseiller caviste expert guidant les clients dans le choix d'un vin selon leurs plats et leur budget."):
        self.agent_name = agent_name
        self.role = role
        self.doctrine = ["Poser impérativement une seule question à la fois.", "Valider avec bienveillance chaque fait collecté.", "Fournir des réponses concises et structurées."]

    def build_system_prompt(self, session_id: str, confirmed_facts: Dict[str, Any], missing_slots: List[str], next_question: str) -> str:
        s0 = f"### SECTION 0 : MÉTA-CONTEXTE\nSession ID: {session_id}\nTimestamp: {datetime.now().isoformat()}"
        s1 = f"### SECTION 1 : IDENTITÉ & DOCTRINE\nNom: {self.agent_name}\nRôle: {self.role}\nDoctrine:\n" + "\n".join(f"- {d}" for d in self.doctrine)
        s2 = f"### SECTION 2 : ÉTAT DES FAITS SCELLÉS (TABLETTE GPS)\nFaits connus: {confirmed_facts}\nSlots manquants: {missing_slots}"
        s3 = "### SECTION 3 : INVARIANTS MÉTIER STRICTS\nRègle: Aucune hallucination tolérée. S'en tenir aux faits scellés."
        s4 = "### SECTION 4 : CONTEXTE RAG & FAQ HÔTE\nConnaissance certifiée injectée depuis les bases documentaires."
        s5 = f"### SECTION 5 : PROCHAINE QUESTION UNIQUE DIRECTE\n{next_question}"
        s6 = "### SECTION 6 : DIRECTIVE FORMAT DE SORTIE JSON STRICT\nRépondre avec concision et professionnalisme."
        return "\n\n".join([s0, s1, s2, s3, s4, s5, s6])
