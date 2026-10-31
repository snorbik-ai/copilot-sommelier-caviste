import os
from typing import List, Dict, Any, Optional

class VectorRetriever:
    """Sous-composant RAG pour interroger des bases documentaires spécifiques avec support Ollama."""
    def __init__(self, ollama_url: Optional[str] = None):
        self.ollama_url = ollama_url or os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

    def search_relevant_context(self, query: str, top_k: int = 3) -> List[Dict[str, Any]]:
        return [
            {"source": "documentation_officielle", "score": 0.95, "text": f"Règle de gouvernance pour : {query}"},
            {"source": "politiques_securite", "score": 0.88, "text": "Seuils opérationnels et validation déterministe."}
        ]
