import os
import json
from pathlib import Path
from typing import Dict, Any, Optional
from copilot_sommelier_caviste.domain.ports.storage_port import IStoragePort

class HostStorageBridge(IStoragePort):
    """Adaptateur de liaison vers la BDD hôte du client (PostgreSQL, Supabase) ou stockage local persistant."""
    def __init__(self, external_client: Optional[Any] = None, storage_dir: Optional[str] = None):
        self.client = external_client
        self.storage_dir = Path(storage_dir or os.getenv("COPILOT_STORAGE_DIR", "./data/host_storage"))

    def save_session(self, session_id: str, data: Dict[str, Any]) -> bool:
        if self.client and hasattr(self.client, "save"):
            return bool(self.client.save(session_id, data))
        self.storage_dir.mkdir(parents=True, exist_ok=True)
        (self.storage_dir / f"{session_id}.json").write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
        return True

    def load_session(self, session_id: str) -> Optional[Dict[str, Any]]:
        if self.client and hasattr(self.client, "load"):
            return self.client.load(session_id)
        f = self.storage_dir / f"{session_id}.json"
        return json.loads(f.read_text(encoding="utf-8")) if f.exists() else None
