import json
import os
from pathlib import Path

def test_notebook_valid_json_and_cells():
    p = Path(__file__).parent.parent / "notebooks" / "01_console_laboratoire_cycle_de_vie_tour_complet_v1.ipynb"
    s = str(p.absolute())
    prefix = chr(92)*2 + "?" + chr(92)
    if os.name == "nt" and not s.startswith(prefix):
        p = Path(prefix + s)
    assert p.exists(), f"Le carnet Jupyter n'existe pas : {p}"
    content = json.loads(p.read_text(encoding="utf-8"))
    assert content["nbformat"] == 4
    assert len(content["cells"]) >= 10, f"Nombre insuffisant de cellules : {len(content['cells'])}"
