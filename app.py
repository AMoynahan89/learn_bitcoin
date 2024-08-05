from flask import Flask, render_template, sessions, jsonify, request
import requests
import sqlite3
import make_db
import block_manager as bm
import os
import qrcode
import base64
from io import BytesIO
import qr_generator as qr

# Configure application
app = Flask(__name__)

# Create database
make_db.main()

#con = sqlite3.connect("database/blocks.db")
#db = con.cursor()


@app.route('/')
def index():    
    return render_template("index.html")


@app.route('/use')
def use():
    return render_template("use.html")


@app.route('/learn')
def learn():
    return render_template("learn.html")


@app.route('/explore', methods=["GET", "POST"])
def explore():
    if request.method == "POST":
        height = request.form.get("block")
        blob = bm.get_blocks_blob(height)
        
        # Parse blob, save new blocks, return clean blocks
        clean_blocks = bm.get_clean_blocks(blob)
        clean_block = clean_blocks[0]
        
        # Return a list of the block heights in clean_blocks
        block_heights = [block["height"] for block in clean_blocks]

        return render_template("explore.html", clean_block=clean_block, block_heights=block_heights)

    else:
        # On page load get 15 most recent blocks
        tip_height = bm.get_tip_height()
        blob = bm.get_blocks_blob(tip_height)

        # Parse blob, save new blocks, return clean blocks
        clean_blocks = bm.get_clean_blocks(blob)
        clean_block = clean_blocks[0]

        # Return a list of the block heights in clean_blocks
        block_heights = [block["height"] for block in clean_blocks]

        return render_template("explore.html", clean_block=clean_block, block_heights=block_heights)


@app.route('/load_block_data')
def load_block_data():
    con = sqlite3.connect("database/blocks.db")
    db = con.cursor()

    height = int(request.args.get("height"))
    db.execute("SELECT * FROM blocks WHERE height = ?", (height,))
    block_data = db.fetchone()
    
    clean_block = {
        'id': block_data[0],
        'height': block_data[1],
        'version': block_data[2],
        'timestamp': block_data[3],
        'bits': block_data[4],
        'nonce': block_data[5],
        'difficulty': block_data[6],
        'merkle_root': block_data[7],
        'tx_count': block_data[8],
        'size': block_data[9],
        'weight': block_data[10],
        'previousblockhash': block_data[11],
        'mediantime': block_data[12],
        'reward': block_data[13],
        'medianFee': block_data[14],
        'totalFees': block_data[15],
        'pool_name': block_data[16]
    }
    con.close()

    return jsonify(clean_block)


@app.route('/donate', methods=["GET", "POST"])
def donate():
    return render_template("donate.html")


@app.route('/make_qr', methods=["GET", "POST"])
def make_qr():
    address = "bc1q2dgdxzum2ctq4mqeyx6yrt4j00pewuk8xzxgmt"
    if request.method == "POST":
        amount = request.form.get("amount")
        print(amount)
        sats = int(amount) / 100000000
        label = "Custom-Donation"

        uri = qr.bit_uri(address, amount=sats, label=label)
        img = qr.make_qr(uri)

        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)
        data = base64.b64encode(buffer.getvalue()).decode()
        
        return jsonify(img=data)

    else:
        amount = request.args.get("amount")
        if amount:
            sats = int(amount) / 100000000
            label = "Custom-Donation"

            uri = qr.bit_uri(address, amount=sats, label=label)
            img = qr.make_qr(uri)

            buffer = BytesIO()
            img.save(buffer, format="PNG")
            buffer.seek(0)
            data = base64.b64encode(buffer.getvalue()).decode()
            
            return jsonify(img=data)

    """
    # Where to save image
    my_dir = os.getcwd()
    file = f"{my_dir}/static/images/address_qr.png"

    # If file exists ... else ...
    if os.path.isfile(file):
        return render_template("donate.html", qr_path=file)
    # If file does not exist creat qr code 
    else:
    """