from flask import Flask, render_template, sessions
import requests

from matplotlib.figure import Figure
#import numpy as np

import os

# Configure application
app = Flask(__name__)


@app.route('/')
def index():

    response = requests.get("https://mempool.space/api/v1/historical-price")

    if response.status_code == 200:
        data = response.json()

    times = [result["time"] for result in data["prices"]]
    prices = [result["USD"] for result in data["prices"]]

    fig = Figure(figsize=(5, 4), dpi=100)

    # Do some plotting
    ax = fig.add_subplot()
    ax.plot(times, prices)

    # Option 1: Save the figure to a file
    image_path = os.path.join(app.root_path, "static/images/test.png")
    fig.savefig(image_path)

    return render_template("index.html", image_url="/static/images/test.png")

@app.route('/intro')
def intro():
    return render_template("intro.html")

@app.route('/guide')
def guide():
    return render_template("guide.html")

@app.route('/technical')
def technical():
    return render_template("technical.html")

@app.route('/history')
def history():

    response = requests.get("https://mempool.space/api/v1/historical-price")

    if response.status_code == 200:
        data = response.json()

    times = [result["time"] for result in data["prices"] if result["USD"] > 0]
    prices = [result["USD"] for result in data["prices"] if result["USD"] > 0]

    fig = Figure(figsize=(5, 2.5), dpi=500)

    # Do some plotting
    ax = fig.add_subplot()
    ax.plot(times, prices)

    # Option 1: Save the figure to a file
    image_path = os.path.join(app.root_path, "static/images/chart.png")
    fig.savefig(image_path)

    return render_template("history.html", image_url="/static/images/chart.png")