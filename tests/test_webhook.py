from copilot_sommelier_caviste.application.webhook_dispatcher import WebhookDispatcherService

def test_webhook_signing_and_payload():
    dispatcher = WebhookDispatcherService(secret_key="test_secret_123")
    payload = dispatcher.build_event_payload("appointment.confirmed", {"ref": "REF-TEST-001"})
    sig = dispatcher.sign_payload(payload)
    assert sig.startswith("sha256=")
    assert len(sig) > 40
