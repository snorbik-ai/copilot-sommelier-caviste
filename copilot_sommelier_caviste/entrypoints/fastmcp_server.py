"""
Serveur MCP STDIO JSON-RPC 2.0 pour Copilot Sommelier & Accords Vins (v22.1).
Expose l'outil 'recommander_accord_mets_vins'.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from copilot_sommelier_caviste.domain.engine import ConseilCavisteEngine

engine = ConseilCavisteEngine()

TOOLS_METADATA = [
    {
        "name": "recommander_accord_mets_vins",
        "description": "Conseil et accords mets-vins personnalisés selon le plat, le budget et les préférences.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "plat": {"type": "string", "description": "Plat ou ingrédient principal (ex: magret de canard, turbot rôti)"},
                "budget_max": {"type": "number", "description": "Budget maximum par bouteille en euros (optionnel)", "default": 35.0},
                "couleur_preferee": {"type": "string", "enum": ["rouge", "blanc", "rose", "effervescent", "indifferent"], "default": "indifferent"}
            },
            "required": ["plat"]
        }
    }
]

def handle_tool_call(name: str, args: dict) -> dict:
    if name == "recommander_accord_mets_vins":
        plat = args.get("plat", "")
        budget = float(args.get("budget_max", 35.0))
        couleur = args.get("couleur_preferee", "indifferent")
        res = engine.evaluate_and_complete({
            "plat": plat,
            "budget_max": budget,
            "couleur_preferee": couleur
        })
        return res.model_dump()
    raise ValueError(f"Outil inconnu : {name}")

def run_stdio_server():
    """Boucle principale JSON-RPC 2.0 canonique universelle sur stdin / stdout (v22.1)."""
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            req_id = req.get("id")
            method = req.get("method")

            # Notification sans id : absorption silencieuse
            if req_id is None:
                continue

            if method == "initialize":
                resp = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "protocolVersion": "2024-11-05",
                        "serverInfo": {
                            "name": "copilot-sommelier-caviste",
                            "version": "1.0.0"
                        },
                        "capabilities": {
                            "tools": {},
                            "resources": {}
                        }
                    }
                }
            elif method == "ping":
                resp = {"jsonrpc": "2.0", "id": req_id, "result": {}}
            elif method == "tools/list":
                resp = {"jsonrpc": "2.0", "id": req_id, "result": {"tools": TOOLS_METADATA}}
            elif method == "tools/call":
                params = req.get("params", {})
                name = params.get("name")
                args = params.get("arguments", {})
                result = handle_tool_call(name, args)
                resp = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {"content": [{"type": "text", "text": json.dumps(result, indent=2, ensure_ascii=False)}]}
                }
            elif method == "resources/list":
                resp = {"jsonrpc": "2.0", "id": req_id, "result": {"resources": []}}
            else:
                resp = {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Method not found: {method}"}}

            sys.stdout.write(json.dumps(resp, ensure_ascii=False) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stderr.write(f"[sommelier error] {e}\n")
            sys.stderr.flush()
            if req_id is not None:
                err_resp = {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32603, "message": str(e)}}
                sys.stdout.write(json.dumps(err_resp, ensure_ascii=False) + "\n")
                sys.stdout.flush()

if __name__ == "__main__":
    run_stdio_server()
