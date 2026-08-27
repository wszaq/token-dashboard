import os
import sqlite3
import tempfile
import unittest
from token_dashboard.db import init_db, connect


class InitDbTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.db_path = os.path.join(self.tmp, "test.db")

    def test_init_creates_expected_tables(self):
        init_db(self.db_path)
        with sqlite3.connect(self.db_path) as c:
            tables = {r[0] for r in c.execute("SELECT name FROM sqlite_master WHERE type='table'")}
        expected = {"files", "messages", "tool_calls", "plan", "dismissed_tips"}
        self.assertTrue(expected.issubset(tables), f"Missing: {expected - tables}")

    def test_init_is_idempotent(self):
        init_db(self.db_path)
        init_db(self.db_path)

    def test_tool_calls_delete_by_message_uuid_uses_index(self):
        """scanner.py runs this DELETE once per message; a SCAN here is quadratic.

        Unindexed, a full 1.1GB cold scan never finished (600 files/320MB = 145s
        against 50 files/42MB = 2s). Guards idx_tools_msg_uuid against removal.
        """
        init_db(self.db_path)
        with sqlite3.connect(self.db_path) as c:
            plan = " ".join(
                str(r[-1]) for r in
                c.execute("EXPLAIN QUERY PLAN DELETE FROM tool_calls WHERE message_uuid=?", ("x",))
            )
        self.assertNotIn("SCAN tool_calls", plan, f"full table scan on hot path: {plan}")
        self.assertIn("idx_tools_msg_uuid", plan, f"expected index unused: {plan}")

    def test_journal_mode_is_wal(self):
        init_db(self.db_path)
        with connect(self.db_path) as c:
            self.assertEqual(c.execute("PRAGMA journal_mode").fetchone()[0].lower(), "wal")

    def test_connect_returns_row_factory(self):
        init_db(self.db_path)
        with connect(self.db_path) as c:
            r = c.execute("SELECT 1 AS one").fetchone()
        self.assertEqual(r["one"], 1)


if __name__ == "__main__":
    unittest.main()
