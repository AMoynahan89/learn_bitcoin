from flask import Flask, render_template, sessions
import requests
from PIL import Image
import numpy as np
import os

from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure


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
    # A canvas must be manually attached to the figure (pyplot would automatically
    # do it).  This is done by instantiating the canvas with the figure as
    # argument.
    canvas = FigureCanvasAgg(fig)

    # Do some plotting.
    ax = fig.add_subplot()
    ax.plot([1, 2, 3])

    # Option 1: Save the figure to a file; can also be a file-like object (BytesIO,
    # etc.).
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
