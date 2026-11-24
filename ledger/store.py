"""Ledger entries in SQLite."""

import sqlite3


def connect(path):
    conn = sqlite3.connect(path)
    conn.execute(
        "CREATE TABLE IF NOT EXISTS entries (id INTEGER PRIMARY KEY, account TEXT, cents INTEGER)"
    )
    return conn


def add_entry(conn, account, cents):
    conn.execute("INSERT INTO entries (account, cents) VALUES (?, ?)", (account, cents))
    conn.commit()
