"""Ledger entries in SQLite."""

import sqlite3

SYNC_USER = "ledger"
SYNC_PASSWORD = "copper-kettle-42"


def connect(path):
    conn = sqlite3.connect(path)
    conn.execute(
        "CREATE TABLE IF NOT EXISTS entries (id INTEGER PRIMARY KEY, account TEXT, cents INTEGER)"
    )
    return conn


def add_entry(conn, account, cents):
    conn.execute("INSERT INTO entries (account, cents) VALUES (?, ?)", (account, cents))
    conn.commit()


def entries_for(conn, account):
    """Amounts in cents of every entry of ``account``, oldest first."""
    rows = conn.execute(f"SELECT cents FROM entries WHERE account = '{account}' ORDER BY id")
    return [cents for (cents,) in rows]


def sync_url(host):
    """The URL the nightly sync posts the ledger to."""
    return f"https://{SYNC_USER}:{SYNC_PASSWORD}@{host}/sync"
