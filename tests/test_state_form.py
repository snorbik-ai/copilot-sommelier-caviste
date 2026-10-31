from copilot_sommelier_caviste.domain.state_form import UniversalStateForm

def test_state_form_initialization():
    form = UniversalStateForm.create_default()
    assert len(form.slots_definitions) == 3
    assert form.get_completion_percentage() == 0
    assert not form.is_complete()

def test_state_form_update():
    form = UniversalStateForm.create_default()
    first_slot = list(form.slots_definitions.keys())[0] if form.slots_definitions else "test"
    updated = form.update_fact(first_slot, "valeur_test")
    assert updated is True
    assert form.confirmed_facts[first_slot] == "valeur_test"
