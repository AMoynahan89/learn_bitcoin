from flask import Flask, render_template
import requests



# Configure application
app = Flask(__name__)


@app.route('/')
def index():
    """
    response = requests.get("https://mempool.space/api/v1/prices")

    if response.status_code == 200:
        raw_price = response.json()
        price = raw_price["USD"]
    return render_template("index.html", price=price)
    """
    return render_template("index.html")

@app.route('/genesis')
def genesis():
    return render_template("genesis.html")

@app.route('/bitcoin')
def bitcoin():
    return render_template("bitcoin.html")

@app.route('/nodes')
def nodes():
    return render_template("nodes.html")

@app.route('/mining')
def mining():
    return render_template("mining.html")

"""
@app.route('/')
def _______():
    return render_template("_______.html")
"""