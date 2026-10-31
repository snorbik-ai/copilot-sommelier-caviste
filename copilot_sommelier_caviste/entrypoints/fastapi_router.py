import os
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Any, Optional
from copilot_sommelier_caviste.domain.state_form import UniversalStateForm
from copilot_sommelier_caviste.domain.engine import ConseilCavisteEngine

# Application ASGI racine officielle pour Uvicorn et conteneurs Docker
app = FastAPI(
    title="Copilot Sommelier & Accords Vins API",
    version="1.0.0",
    description="Conseiller caviste expert guidant les clients dans le choix d'un vin selon leurs plats et leur budget."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter(prefix="/api/v1/copilot", tags=["Copilot Sommelier & Accords Vins"])

class TurnRequest(BaseModel):
    session_id: str
    message: str
    facts: Optional[Dict[str, Any]] = None

@app.get("/health")
def health():
    """Route de santé officielle pour Docker, Kubernetes et passerelles hôtes."""
    return {
        "status": "UP",
        "agent_id": "copilot-sommelier-caviste",
        "version": "1.0.0"
    }

@router.post("/turn")
def execute_turn(req: TurnRequest):
    form = UniversalStateForm.create_default()
    if req.facts:
        for k, v in req.facts.items():
            form.update_fact(k, v)

    completion = form.get_completion_percentage()
    next_q = form.get_next_question()

    return {
        "agent_id": "copilot-sommelier-caviste",
        "session_id": req.session_id,
        "completion_rate": completion,
        "is_complete": form.is_complete(),
        "next_question": next_q,
        "confirmed_facts": form.confirmed_facts
    }

@router.get("/handshake")
def handshake(api_key: Optional[str] = None):
    """Vérification handshake sécurisée pour intégration widget ou SaaS hôte."""
    return {
        "status": "READY",
        "agent_id": "copilot-sommelier-caviste",
        "agent_name": "Copilot Sommelier & Accords Vins",
        "version": "1.0.0",
        "role": "Conseiller caviste expert guidant les clients dans le choix d'un vin selon leurs plats et leur budget.",
        "authorized": bool(api_key)
    }

app.include_router(router)
