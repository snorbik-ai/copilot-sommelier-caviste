import json
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional

@dataclass
class SlotDefinition:
    name: str
    label: str
    slot_type: str
    mandatory: bool
    question: str
    choices: Optional[List[str]] = None
    min_value: Optional[float] = None
    max_value: Optional[float] = None

@dataclass
class UniversalStateForm:
    """Moteur d'état universel gérant les slots et le cycle de vie FSM."""
    slots_definitions: Dict[str, SlotDefinition] = field(default_factory=dict)
    confirmed_facts: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def create_default(cls) -> "UniversalStateForm":
        raw_slots = json.loads('''[
    {
        "name": "type_plat",
        "label": "Plat ou Mets Accompagné",
        "slot_type": "string",
        "required": true,
        "elicitation_question": "Quel plat ou type de cuisine souhaitez-vous accompagner (ex: viande rouge, poisson, fromage) ?",
        "choices": null,
        "min_value": null,
        "max_value": null
    },
    {
        "name": "couleur_preferee",
        "label": "Couleur de Vin",
        "slot_type": "choice",
        "required": true,
        "elicitation_question": "Avez-vous une préférence de couleur ?",
        "choices": [
            {
                "key": "rouge",
                "label": "Vin Rouge"
            },
            {
                "key": "blanc",
                "label": "Vin Blanc"
            },
            {
                "key": "rose",
                "label": "Vin Rosé"
            },
            {
                "key": "bulles",
                "label": "Champagne / Bulles"
            }
        ],
        "min_value": null,
        "max_value": null
    },
    {
        "name": "budget_max",
        "label": "Budget par Bouteille (€)",
        "slot_type": "number",
        "required": true,
        "elicitation_question": "Quel est votre budget indicatif par bouteille en euros ?",
        "choices": null,
        "min_value": null,
        "max_value": null
    }
]''')
        form = cls()
        for s in raw_slots:
            form.slots_definitions[s["name"]] = SlotDefinition(
                name=s["name"],
                label=s["label"],
                slot_type=s["slot_type"],
                mandatory=s.get("required", True),
                question=s["elicitation_question"],
                choices=[c for c in s.get("choices", [])] if s.get("choices") else None,
                min_value=s.get("min_value"),
                max_value=s.get("max_value"),
            )
        return form

    def update_fact(self, key: str, value: Any) -> bool:
        if key in self.slots_definitions and value is not None:
            self.confirmed_facts[key] = value
            return True
        return False

    def get_missing_slots(self) -> List[SlotDefinition]:
        return [s for s in self.slots_definitions.values() if s.mandatory and s.name not in self.confirmed_facts]

    def is_complete(self) -> bool:
        return len(self.get_missing_slots()) == 0

    def get_completion_percentage(self) -> int:
        mandatory = [s for s in self.slots_definitions.values() if s.mandatory]
        if not mandatory:
            return 100
        completed = sum(1 for s in mandatory if s.name in self.confirmed_facts)
        return int((completed / len(mandatory)) * 100)

    def get_next_question(self) -> Optional[str]:
        missing = self.get_missing_slots()
        return missing[0].question if missing else None
