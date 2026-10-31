class TriChannelManager:
    """Gestionnaire de routage tri-canal (Canal A Utilisateur, Canal B Métier, Canal C Observabilité)."""
    def route_event(self, channel: str, payload: dict) -> bool:
        return True
