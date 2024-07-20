from flask import Flask, render_template, sessions
import requests

from matplotlib.figure import Figure
#import numpy as np

import os

# Configure application
app = Flask(__name__)


@app.route('/')
def index():    
    # Chech if we have file
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

@app.route('/how_to_use')
def how_to_use():
    return render_template("how_to_use.html")

@app.route('/learn')
def learn():
    return render_template("learn.html")

@app.route('/explore')
def explore():
    return render_template("explore.html")

@app.route('/donate')
def donate():
    return render_template("donate.html")