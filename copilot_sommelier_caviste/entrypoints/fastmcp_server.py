"""Serveur FastMCP STDIO pour Copilot Sommelier & Accords Vins."""
import sys
from copilot_sommelier_caviste.domain.state_form import UniversalStateForm

def run_stdio_server():
    form = UniversalStateForm.create_default()
    print(f"Serveur FastMCP initialisé pour 'Copilot Sommelier & Accords Vins' (1.0.0)", file=sys.stderr)

if __name__ == "__main__":
    run_stdio_server()
