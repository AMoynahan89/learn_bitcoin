import requests
import sqlite3


# Create database and create cursor object
#db.initialize_db()
#con = sqlite3.connect("database/blocks.db")
#db = con.cursor()


# Get current block height
def get_tip_height():
    response = requests.get("https://mempool.space/api/blocks/tip/height")
    tip_height = int(response.text)
    return tip_height


# Get block data of block #(block_height) and 14 previous blocks
def get_blocks_blob(block_height) -> tuple:
    response = requests.get(f"https://mempool.space/api/v1/blocks/{block_height}")
    return response.json()


# Parse block and return block with desired data only. Returns a list of dictionaries.
def parse_block(block) -> dict:
    clean_block = {}
    # Establish desired keys
    keys = [
        "id", 
        "height", 
        "version", 
        "timestamp", 
        "bits", 
        "nonce", 
        "difficulty", 
        "merkle_root", 
        "tx_count", 
        "size", 
        "weight", 
        "previousblockhash", 
        "mediantime", 
        "extras"
    ]   

    # Extract desired "extras" values and establish those desired sub_keys
    block_extras = block["extras"]
    extras = [
        "reward",
        "medianFee",
        "totalFees",   
        "pool"
    ]

    # Extract desired values and asign only desired dictionaries to clean_block list
    for key in keys:
        if key == "extras":
            for sub_key in extras:
                if sub_key == "pool":
                    pool_data = block_extras[sub_key]
                    pool_name = pool_data["name"]
                    clean_block["pool_name"] = pool_name
                else:
                    clean_block[sub_key] = block_extras[sub_key]
        else:        
            clean_block[key] = block[key]

    return clean_block


# Parse blocks and store block data to database
def get_clean_blocks(blocks_blob) -> list:
    con = sqlite3.connect("database/blocks.db")
    db = con.cursor()

    clean_blocks = []

    # Iterate over list of raw blocks
    for block in blocks_blob:
        block_height = int(block["height"])

        #Check if block is in database
        row = (db.execute("SELECT * FROM blocks WHERE height = ?", (block_height,))).fetchall()
        #print(row)
        if not row:
            clean_block = parse_block(block)
            store_block_data(clean_block)
            clean_blocks.append(clean_block)
            #print("Stored new block:", block_height)
        else:
            clean_block = parse_block(block)
            clean_blocks.append(clean_block)
            #print("Block already in database:", block_height)
        #print(len(clean_blocks))
    
    con.close()
    return clean_blocks


#Stores block data of 1 block at a time
def store_block_data(clean_block) -> None:
    con = sqlite3.connect("database/blocks.db")
    db = con.cursor()
    # Extract the values from the dictionary in the required order
    block_data = [
        clean_block["id"],
        clean_block["height"],
        clean_block["version"],
        clean_block["timestamp"],
        clean_block["bits"],
        clean_block["nonce"],
        clean_block["difficulty"],
        clean_block["merkle_root"],
        clean_block["tx_count"],
        clean_block["size"],
        clean_block["weight"],
        clean_block["previousblockhash"],
        clean_block["mediantime"],
        clean_block["totalFees"],
        clean_block["medianFee"],
        clean_block["reward"],
        clean_block["pool_name"]
    ]

    # Insert the values into the database
    db.execute("""
        INSERT INTO blocks (
            id, 
            height, 
            version, 
            timestamp, 
            bits, 
            nonce, 
            difficulty, 
            merkle_root, 
            tx_count, 
            size, 
            weight, 
            previousblockhash, 
            mediantime, 
            totalFees, 
            medianFee, 
            reward, 
            pool_name
        ) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, block_data)
    con.commit()
    con.close()





# App GET request on page load
def main():
    tip_height = get_tip_height()
    blocks_blob = get_blocks_blob(tip_height)
    clean_blocks = get_clean_blocks(blocks_blob)
    return clean_blocks


main()



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




height = block["height"]
db.execute("SELECT * FROM block WHERE height = ?", height)

times = [result["time"] for result in data["prices"] if result["USD"] == 0]
"""

"""
    # Chech if file exists
    my_dir = os.getcwd()
    with os.scandir(f"{my_dir}/static/images") as dir:
        for file in dir:
            if file.name.startswith('test') and file.is_file():
                return render_template("index.html", image_url="/static/images/test.png")
                
        response = requests.get("https://mempool.space/api/v1/historical-price")

        if response.status_code == 200:
            data = response.json()

        times = [result["time"] for result in data["prices"] if result["USD"] > 0]
        prices = [result["USD"] for result in data["prices"] if result["USD"] > 0]

        fig = Figure(figsize=(5, 4), dpi=100)

        # Do some plotting
        ax = fig.add_subplot()
        ax.plot(times, prices)

        # Option 1: Save the figure to a file
        image_path = os.path.join(app.root_path, "static/images/test.png")
        fig.savefig(image_path)
    return render_template("index.html", image_url="/static/images/test.png")
"""