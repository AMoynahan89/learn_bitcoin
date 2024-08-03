from flask import Flask, render_template, sessions, jsonify, request
import requests
import sqlite3
import make_db
import block_manager as bm
import os
import qrcode


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


@app.route('/donate')
def donate():
    # Where to save image
    my_dir = os.getcwd()
    file = f"{my_dir}/static/images/address_qr.png"

    # If file exists ... else ...
    if os.path.isfile(file):
        return render_template("donate.html", qr_path=file)
    # If file does not exist creat qr code 
    else:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data('bc1qvgz5skmf9etdggqqharkvyf9weczefwumxw5yf')
        qr.make(fit=True)

        img = qr.make_image(back_color=(255, 165, 0), fill_color=(41, 39, 39))
        img.save(file)

        return render_template("donate.html", qr_path=file)




"""
    # Check if file exists
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