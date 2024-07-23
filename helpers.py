"""
# from flask import Flask, sessions
import requests

import datetime
from tzlocal import get_localzone


def local_time(unix):
    utc_time = datetime.datetime.fromtimestamp(unix, tz=datetime.timezone.utc)
    local_tz = get_localzone()
    print(local_tz)
    local_time = utc_time.astimezone(local_tz)
    print(local_time)

local_time(1721757096)
"""
"""
import requests


response = requests.get("https://mempool.space/api/blocks/tip/hash")

current_block_hash = response.text

def get_block(block_hash):
    api = f"https://mempool.space/api/block/{block_hash}"

    response = requests.get(api)
    block = response.json()

    print(block)

get_block(current_block_hash)
"""


import sqlite3
import make_db

# Configure application
app = Flask(__name__)

# Create database and cursor object
make_db.initialize_db()
db = make_db.connect("database/block.db")
