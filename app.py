from flask import Flask, render_template, sessions, jsonify, request
import requests
import sqlite3

import make_db
import block_manager as bm

from matplotlib.figure import Figure

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


@app.route('/explore')
def explore():
    # On page load get 15 most recent blocks
    tip_height = bm.get_tip_height()
    blob = bm.get_blocks_blob(tip_height)

    # Parse blob, save new blocks, return clean blocks
    clean_blocks = bm.get_clean_blocks(blob)
    #clean_blocks = [{'id': '000000000000000000028674d664b83fe9f1d1cd88680327fc2fd709135336e8', 'height': 854087, 'version': 839106560, 'timestamp': 1722027727, 'bits': 386100794, 'nonce': 2146407034, 'difficulty': 82047728459932.75, 'merkle_root': 'e9ccd039d6c2afc591f69e588471c05db265bae560e7347aadb5f1aeb4e1e9f5', 'tx_count': 4585, 'size': 1579943, 'weight': 3997904, 'previousblockhash': '0000000000000000000343c8b1338bfe49699714e5e8eb8e3ac78779024db5bc', 'mediantime': 1722024085, 'reward': 317854612, 'medianFee': 3.9863267539417744, 'totalFees': 5354612, 'pool_name': 'F2Pool'}, {'id': '0000000000000000000343c8b1338bfe49699714e5e8eb8e3ac78779024db5bc', 'height': 854086, 'version': 647020544, 'timestamp': 1722027257, 'bits': 386100794, 'nonce': 739947847, 'difficulty': 82047728459932.75, 'merkle_root': '3d3fdc7de24c8ab04989872f45dd18df92a8a64b0af2f297984fe154b87213ff', 'tx_count': 5411, 'size': 1586960, 'weight': 3993032, 'previousblockhash': '0000000000000000000089454da350249f1e54ddc370d3fbd3a5e827153c4b09', 'mediantime': 1722023552, 'reward': 317798226, 'medianFee': 3.6056338028169006, 'totalFees': 5298226, 'pool_name': 'Foundry USA'}, {'id': '0000000000000000000089454da350249f1e54ddc370d3fbd3a5e827153c4b09', 'height': 854085, 'version': 689635328, 'timestamp': 1722026942, 'bits': 386100794, 'nonce': 4256558612, 'difficulty': 82047728459932.75, 'merkle_root': '01af115d8e4a64e2f8cbab132f1c4e25f55ebce058079507820e9a66b4801b8f', 'tx_count': 2945, 'size': 1708434, 'weight': 3993453, 'previousblockhash': '000000000000000000016aad4521518bfc3774ee1a9ed994a05451c1fa04455d', 'mediantime': 1722023268, 'reward': 317616940, 'medianFee': 4.233784588988285, 'totalFees': 5116940, 'pool_name': 'ViaBTC'}, {'id': '000000000000000000016aad4521518bfc3774ee1a9ed994a05451c1fa04455d', 'height': 854084, 'version': 1073733632, 'timestamp': 1722026795, 'bits': 386100794, 'nonce': 407883430, 'difficulty': 82047728459932.75, 'merkle_root': 'edd8aede6b0b48cdbb302f2cdbb6609968bb5385a974e819f7d8b01b94d5a466', 'tx_count': 2999, 'size': 1511595, 'weight': 3997728, 'previousblockhash': '00000000000000000001260ab961aac9c4d292b17e8c27289f0c73c8f235e519', 'mediantime': 1722023103, 'reward': 319589485, 'medianFee': 6, 'totalFees': 7089485, 'pool_name': 'F2Pool'}, {'id': '00000000000000000001260ab961aac9c4d292b17e8c27289f0c73c8f235e519', 'height': 854083, 'version': 593944576, 'timestamp': 1722026419, 'bits': 386100794, 'nonce': 2259671312, 'difficulty': 82047728459932.75, 'merkle_root': 'dc9bc1c0f949b6c9fbd4a7179646027ad880a205c14c29551005a0f6c3580cc2', 'tx_count': 2694, 'size': 1518309, 'weight': 3993234, 'previousblockhash': '000000000000000000012028f46b614a5052013d16ccd0bb4ca35fd3b0e91d24', 'mediantime': 1722022990, 'reward': 326014308, 'medianFee': 7.700471715326183, 'totalFees': 13514308, 'pool_name': 'Foundry USA'}, 
    #{'id': '000000000000000000012028f46b614a5052013d16ccd0bb4ca35fd3b0e91d24', 'height': 854082, 'version': 619913216, 'timestamp': 1722024085, 'bits': 386100794, 'nonce': 4007689293, 'difficulty': 82047728459932.75, 'merkle_root': 'f93fa836bb43fc0b4dda8383e07799e9677b3abfb3ea025019d14d3fc3f2d88f', 'tx_count': 4828, 'size': 1527672, 'weight': 3992964, 'previousblockhash': '0000000000000000000145228b6c3216e9250444d8ba44cff91798c2ed437244', 'mediantime': 1722022550, 'reward': 317772221, 'medianFee': 3.559055118110236, 'totalFees': 5272221, 'pool_name': 'Foundry USA'}, {'id': '0000000000000000000145228b6c3216e9250444d8ba44cff91798c2ed437244', 'height': 854081, 'version': 795385856, 'timestamp': 1722023552, 'bits': 386100794, 'nonce': 1437880935, 'difficulty': 82047728459932.75, 'merkle_root': 'ba4aefc8495db5a14453958a25e7aa1ba5b2e2a8e3ee68f59a0c5880100704b3', 'tx_count': 4986, 'size': 1595567, 'weight': 3992939, 'previousblockhash': '000000000000000000003e4e4eb80615adfa5e5ec3d23b487d9b83007ce08490', 'mediantime': 1722022336, 'reward': 317229517, 'medianFee': 3.601656752098738, 'totalFees': 4729517, 'pool_name': 'Foundry USA'}, {'id': '000000000000000000003e4e4eb80615adfa5e5ec3d23b487d9b83007ce08490', 'height': 854080, 'version': 774119424, 'timestamp': 1722023268, 'bits': 386100794, 'nonce': 457948206, 'difficulty': 82047728459932.75, 'merkle_root': '3949c344dd6ab1bf2abf52c917e0a492a24b3f356208a258ee870efaf6943056', 'tx_count': 2030, 'size': 1514960, 'weight': 3992744, 'previousblockhash': '000000000000000000029757fc7a557a49df07c8bd6d8da3a357de9c616c4709', 'mediantime': 1722021863, 'reward': 316823345, 'medianFee': 3.639597252281923, 'totalFees': 4323345, 'pool_name': 'Carbon Negative'}, {'id': '000000000000000000029757fc7a557a49df07c8bd6d8da3a357de9c616c4709', 'height': 854079, 'version': 744505344, 'timestamp': 1722023103, 'bits': 386100794, 'nonce': 
    #1967001860, 'difficulty': 82047728459932.75, 'merkle_root': '2d85b1a397012c39991061de66c8868a4f7754594083ca76b0a3be8c640600fc', 'tx_count': 1812, 'size': 1992351, 'weight': 3992913, 'previousblockhash': '000000000000000000008ddb9662c6410ea57ae5a09383a6491bbbc2072b4e44', 'mediantime': 1722021838, 'reward': 316965802, 'medianFee': 3.97742592882897, 'totalFees': 4465802, 'pool_name': 'Foundry USA'}, {'id': '000000000000000000008ddb9662c6410ea57ae5a09383a6491bbbc2072b4e44', 'height': 854078, 'version': 633765888, 'timestamp': 1722022990, 'bits': 386100794, 'nonce': 2806149193, 'difficulty': 82047728459932.75, 'merkle_root': 'bf1cf315694f427db6793b86b04e52f825e2dc57a8378a5fd522e27518213b45', 'tx_count': 1801, 'size': 1913352, 'weight': 3993219, 'previousblockhash': '000000000000000000020c9c1cefedea0d8d0a42d749ebe9074f8b6e4d22a5d4', 'mediantime': 1722020734, 'reward': 318572836, 'medianFee': 3.998311058892642, 'totalFees': 6072836, 'pool_name': 'Foundry USA'}, {'id': '000000000000000000020c9c1cefedea0d8d0a42d749ebe9074f8b6e4d22a5d4', 'height': 854077, 'version': 836435968, 'timestamp': 1722022550, 'bits': 386100794, 'nonce': 2538057844, 'difficulty': 82047728459932.75, 'merkle_root': 'a83a2693e9abf93d5659206d65baa489acb3456e1f0b0790e2a9ae0bc0cad0e8', 'tx_count': 1425, 'size': 1996402, 'weight': 3993784, 'previousblockhash': '000000000000000000008cbf72c6881b86648b74763e1fb5020b8eac95b3d319', 'mediantime': 1722020708, 'reward': 317507775, 'medianFee': 3.9999411115200587, 'totalFees': 5007775, 'pool_name': 'AntPool'}, {'id': '000000000000000000008cbf72c6881b86648b74763e1fb5020b8eac95b3d319', 'height': 854076, 'version': 747339776, 'timestamp': 1722022336, 'bits': 386100794, 'nonce': 218197362, 'difficulty': 82047728459932.75, 'merkle_root': '65c7b0706e9c453bf53f6e0c5a8c859faf7a5e53b40788d4d386816c68826e51', 'tx_count': 2164, 'size': 1882203, 'weight': 3992904, 'previousblockhash': '000000000000000000016ae762af2b7ca85748e7faa752627579f1b413de48fb', 'mediantime': 1722018963, 'reward': 318566709, 'medianFee': 4, 'totalFees': 6066709, 'pool_name': 'Foundry USA'}, {'id': '000000000000000000016ae762af2b7ca85748e7faa752627579f1b413de48fb', 'height': 854075, 'version': 
    #856637440, 'timestamp': 1722021863, 'bits': 386100794, 'nonce': 1766814329, 'difficulty': 82047728459932.75, 'merkle_root': 'a8cdc1d13b4113d521f33870db3585a5343f4727ab0ca62de7924b8f780b8267', 'tx_count': 548, 'size': 2152834, 'weight': 3993157, 'previousblockhash': '000000000000000000036cddeef2b6aca38b5f90f6ff03699298d0e149def54c', 'mediantime': 1722018494, 'reward': 316571904, 'medianFee': 4.000058890213919, 'totalFees': 4071904, 'pool_name': 'Foundry USA'}, {'id': '000000000000000000036cddeef2b6aca38b5f90f6ff03699298d0e149def54c', 'height': 854074, 'version': 615825408, 'timestamp': 1722021838, 'bits': 386100794, 'nonce': 3735169036, 'difficulty': 82047728459932.75, 'merkle_root': '8d03d8d6d5cf1dfb9728ba88adf0286b13cd72d37df854b9337b493e4d2b28ab', 'tx_count': 3923, 'size': 1638987, 'weight': 3997848, 'previousblockhash': '00000000000000000000d3ca0edcb256677ffe8cfadfe0f8b7f1ab309068e09a', 'mediantime': 1722018148, 'reward': 
    #324292346, 'medianFee': 6.006457901791154, 'totalFees': 11792346, 'pool_name': 'F2Pool'}, {'id': '00000000000000000000d3ca0edcb256677ffe8cfadfe0f8b7f1ab309068e09a', 'height': 854073, 'version': 538034176, 'timestamp': 1722020734, 'bits': 386100794, 'nonce': 4059522258, 'difficulty': 82047728459932.75, 'merkle_root': '673b36f07fb403386efccd0b597d95c92b3357a18c31561365a0a0e3eaf55ad1', 'tx_count': 2530, 'size': 1537958, 'weight': 3993548, 'previousblockhash': '00000000000000000000af81f0f2883a7e35af482cbdd7f42badb125beed88e6', 'mediantime': 1722017914, 'reward': 317958359, 'medianFee': 5.515941699655409, 'totalFees': 5458359, 'pool_name': 'AntPool'}]

    clean_block = clean_blocks[0]
    #clean_block = next(block for block in clean_blocks if block["height"] == tip_height)
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