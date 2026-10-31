from copilot_sommelier_caviste.application.context_pipeline_builder import ContextPipelineBuilder

def test_context_pipeline_sections():
    builder = ContextPipelineBuilder()
    prompt = builder.build_system_prompt("SES-1", {"slot1": "val1"}, ["slot2"], "Quelle date ?")
    for sec in ["SECTION 0", "SECTION 1", "SECTION 2", "SECTION 3", "SECTION 4", "SECTION 5", "SECTION 6"]:
        assert sec in prompt
