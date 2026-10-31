import os
import hmac
import hashlib
import json
import time
from typing import Dict, Any, Optional

class WebhookDispatcherService:
    """Service d'émission de Webhooks HTTP signés HMAC-SHA256 vers les serveurs hôtes clients."""
    def __init__(self, secret_key: Optional[str] = None):
        self.secret_key = secret_key or os.getenv("COPILOT_WEBHOOK_SECRET", "default_secret_key")

    def sign_payload(self, payload: Dict[str, Any]) -> str:
        body = json.dumps(payload, sort_keys=True)
        sig = hmac.new(self.secret_key.encode("utf-8"), body.encode("utf-8"), hashlib.sha256).hexdigest()
        return f"sha256={sig}"

    def build_event_payload(self, event_type: str, data: Dict[str, Any]) -> Dict[str, Any]:
        return {"event": event_type, "timestamp": int(time.time()), "data": data}
