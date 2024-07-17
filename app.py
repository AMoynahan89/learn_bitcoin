from flask import Flask, render_template, sessions
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