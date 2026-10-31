from abc import ABC, abstractmethod
from typing import Dict, Any, Optional

class IStoragePort(ABC):
    """Port hexagonal pour la persistance des sessions et des états copilote."""
    @abstractmethod
    def save_session(self, session_id: str, data: Dict[str, Any]) -> bool:
        pass

    @abstractmethod
    def load_session(self, session_id: str) -> Optional[Dict[str, Any]]:
        pass
