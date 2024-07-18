from flask import Flask, render_template, sessions
import requests

from matplotlib.figure import Figure
#import numpy as np

import os

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

    fig = Figure(figsize=(5, 4), dpi=100)
    

    # Do some plotting
    ax = fig.add_subplot()
    ax.plot([1, 2, 3, 4], [0, 10, 20, 40])

    # Option 1: Save the figure to a file
    image_path = os.path.join(app.root_path, "static/images/test.png")
    fig.savefig(image_path)

    return render_template("index.html", image_url="/static/images/test.png")

@app.route('/intro')
def intro():
    return render_template("intro.html")

@app.route('/get_started')
def get_started():
    return render_template("get_started.html")

@app.route('/guide')
def guide():
    return render_template("guide.html")

@app.route('/technical')
def technical():
    return render_template("technical.html")

@app.route('/history')
def history():
    return render_template("history.html")
