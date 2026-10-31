import os
import sqlite3
import json
import time
from typing import Dict, Any, Optional

class SQLiteCacheAdapter:
    """Cache de session local en mode WAL pour performances < 2ms avec verrouillage anti-collision."""
    def __init__(self, db_path: Optional[str] = None):
        resolved_path = db_path or os.getenv("COPILOT_DB_PATH", ":memory:")
        self.conn = sqlite3.connect(resolved_path, check_same_thread=False)
        self.conn.execute("PRAGMA journal_mode=WAL;")
        self.conn.execute("CREATE TABLE IF NOT EXISTS sessions (id TEXT PRIMARY KEY, data TEXT);")
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS slot_locks (
                lock_id TEXT PRIMARY KEY,
                session_id TEXT,
                slot_date TEXT,
                time_slot TEXT,
                expires_at REAL
            );
        """)
        self.conn.commit()

    def save_session(self, session_id: str, data: Dict[str, Any]) -> bool:
        payload = json.dumps(data)
        self.conn.execute("INSERT OR REPLACE INTO sessions (id, data) VALUES (?, ?);", (session_id, payload))
        self.conn.commit()
        return True

    def load_session(self, session_id: str) -> Optional[Dict[str, Any]]:
        cur = self.conn.cursor()
        cur.execute("SELECT data FROM sessions WHERE id = ?;", (session_id,))
        row = cur.fetchone()
        return json.loads(row[0]) if row else None

    def auto_purge_expired_locks(self) -> int:
        now = time.time()
        cur = self.conn.cursor()
        cur.execute("DELETE FROM slot_locks WHERE expires_at < ?;", (now,))
        purged = cur.rowcount
        self.conn.commit()
        return purged

    def hold_slot(self, session_id: str, slot_date: str, time_slot: str, ttl_seconds: int = 600) -> bool:
        self.auto_purge_expired_locks()
        cur = self.conn.cursor()
        cur.execute("SELECT session_id FROM slot_locks WHERE slot_date = ? AND time_slot = ?;", (slot_date, time_slot))
        row = cur.fetchone()
        if row and row[0] != session_id:
            return False
        expires_at = time.time() + ttl_seconds
        lock_id = f"LOCK-{slot_date}-{time_slot}"
        self.conn.execute(
            "INSERT OR REPLACE INTO slot_locks (lock_id, session_id, slot_date, time_slot, expires_at) VALUES (?, ?, ?, ?, ?);",
            (lock_id, session_id, slot_date, time_slot, expires_at)
        )
        self.conn.commit()
        return True

    def is_slot_locked(self, slot_date: str, time_slot: str) -> bool:
        self.auto_purge_expired_locks()
        cur = self.conn.cursor()
        cur.execute("SELECT 1 FROM slot_locks WHERE slot_date = ? AND time_slot = ?;", (slot_date, time_slot))
        return cur.fetchone() is not None
