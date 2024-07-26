from flask import Flask, render_template, sessions
import requests

import sqlite3
import make_db

from matplotlib.figure import Figure

# Configure application
app = Flask(__name__)

# Create database
make_db.main()

con = sqlite3.connect("database/blocks.db")
db = con.cursor()


@app.route('/')
def index():    
    return render_template("index.html")

@app.route('/use')
def use():
    return render_template("use.html")

@app.route('/learn')
def learn():
    return render_template("learn.html")

@app.route('/explore')
def explore():
    clean_block = {
        'id': '000000000000000000006b6e8dc5bd815c1f661581c38e0bb4c7fd2d54d272fc',
        'height': 854065,
        'version': 625696768,
        'timestamp': 1722015977,
        'bits': 386100794,
        'nonce': 225334596,
        'difficulty': 82047728459932.75,
        'merkle_root': 'cf657e555b5eeacbe206d9544e2a215a373d87d738da0e48b7e04656bd620ec8',
        'tx_count': 771,
        'size': 1997014,
        'weight': 3993160,
        'previousblockhash': '0000000000000000000251755b34dd490d7fe315730e6f4209ef9cb6b3feea07',
        'mediantime': 1722013984,
        'reward': 317227675,
        'medianFee': 4.000235571260307,
        'totalFees': 4727675,
        'pool_name': 'ViaBTC'
    }


    return render_template("explore.html", clean_block=clean_block)

@app.route('/donate')
def donate():
    return render_template("donate.html")




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