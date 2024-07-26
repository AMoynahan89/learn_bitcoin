import sqlite3


def main():
    con = sqlite3.connect("database/blocks.db")
    db = con.cursor()

    # Create block database
    db.execute("""
    CREATE TABLE IF NOT EXISTS blocks (
        id TEXT PRIMARY KEY,
        height INT,
        version INT,
        timestamp TIMESTAMP,
        bits INT,
        nonce BIGINT,
        difficulty FLOAT,
        merkle_root TEXT,
        tx_count INT,
        size INT,
        weight INT,
        previousblockhash TEXT,
        mediantime TIMESTAMP,
        totalFees BIGINT,
        medianFee INT,
        reward BIGINT,
        pool_name TEXT
    )
    """)
    
    # Index by block height
    db.execute("CREATE INDEX IF NOT EXISTS idx_blocks_height ON blocks(height)")

    con.commit()
    con.close()


if __name__ == "__main__":
    main()