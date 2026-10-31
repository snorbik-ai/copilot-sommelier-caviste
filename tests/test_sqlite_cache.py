from copilot_sommelier_caviste.adapters.persistence.sqlite_cache_adapter import SQLiteCacheAdapter

def test_sqlite_cache_roundtrip():
    cache = SQLiteCacheAdapter(":memory:")
    cache.save_session("SES-123", {"completion": 80})
    loaded = cache.load_session("SES-123")
    assert loaded is not None
    assert loaded["completion"] == 80

def test_sqlite_slot_locking_and_auto_purge():
    cache = SQLiteCacheAdapter(":memory:")
    assert cache.hold_slot("SES-A", "2026-11-04", "10:20", ttl_seconds=600) is True
    assert cache.is_slot_locked("2026-11-04", "10:20") is True
    assert cache.hold_slot("SES-B", "2026-11-04", "10:20", ttl_seconds=600) is False
    assert cache.hold_slot("SES-EXP", "2026-11-04", "14:40", ttl_seconds=-1) is True
    purged = cache.auto_purge_expired_locks()
    assert purged >= 1
    assert cache.is_slot_locked("2026-11-04", "14:40") is False
