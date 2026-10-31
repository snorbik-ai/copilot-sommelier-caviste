from copilot_sommelier_caviste.domain.engine import ConseilCavisteEngine

def test_engine_execution():
    engine = ConseilCavisteEngine()
    result = engine.execute("SESSION-TEST-001", {"montant": 100})
    assert result.success is True
    assert result.status_code == "EXECUTION_CONFIRMED"

def test_engine_generic_validation():
    engine = ConseilCavisteEngine()
    assert len(engine.validate_facts({"montant": 100})) == 0
    assert len(engine.validate_facts({"montant": -50})) > 0
