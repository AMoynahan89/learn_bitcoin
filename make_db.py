import sqlite3


def initialize_db():
    db.execute("""
    CREATE TABLE IF NOT EXISTS block (
        height INTEGER PRIMARY KEY, 
        id TEXT, 
        version INTEGER,
        timestamp INTEGER,
        tx_count INTEGER,
        size INTEGER,
        weight INTEGER,
        merkle_root TEXT,
        previousblockhash TEXT,
        mediantime INTEGER,
        nonce INTEGER,
        bits INTEGER,
        difficulty FLOAT
    )
    """)


def connect(db_path):
    con = sqlite3.connect(db_path)
    db = con.cursor()
    return db





