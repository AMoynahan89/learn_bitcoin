from flask import Flask, render_template, request

# Configure application
app = Flask(__name__)

"""
# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
"""

@app.route('/')
def home():
        return render_template("index.html")

@app.route('/genesis', methods=['POST'])
def genesis():
    return render_template("genesis.html")

"""
@app.route('/button1', methods=['POST'])
def button1():
"""     

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