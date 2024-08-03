"""
import os

my_dir = os.getcwd()

with os.scandir(f"{my_dir}/static/images") as dir:
    for file in dir:
        if file.name.startswith('test') and file.is_file():
            print(file.name)


import os

my_dir = os.getcwd()
file = f"{my_dir}/static/images/test.png"

if os.path.isfile(file):
    print(file)
"""



"""
import matplotlib.pyplot as plt
import numpy as np
import requests


def usd(n):
    n = f"${n:,.2f}"
    return n

response = requests.get("https://mempool.space/api/v1/historical-price")
data = response.json()

times = [result["time"] for result in data["prices"] if result["USD"] == 0]
prices = [result["USD"] for result in data["prices"] if result["USD"] == 0]




fig, ax = plt.subplots()             # Create a figure containing a single Axes.
ax.plot(times, prices)               # Plot some data on the Axes.
plt.show()                           # Show the figure.
"""


"""
{
  prices: [
    {
      "time": 1499904000,
      "EUR": 1964,
      "USD": 2254.9
    }
  ],
  exchangeRates: {
    "USDEUR": 0.92,
    "USDGBP": 0.78,
    "USDCAD": 1.36,
    "USDCHF": 0.89,
    "USDAUD": 1.53,
    "USDJPY": 149.48
  }
}
"""






"""
def parse_block(block) -> list:
    clean_block = []
    # Establish desired keys
    keys = [
        "id", 
        "height", 
        "version", 
        "timestamp", 
        "bits", 
        "nonce", 
        "difficulty", 
        "merkle_root", 
        "tx_count", 
        "size", 
        "weight", 
        "previousblockhash", 
        "mediantime", 
        "extras"
    ]   

    # Extract desired "extras" values and establish those desired sub_keys
    block_extras = block["extras"]
    extras = [
        "reward",
        "medianFee",
        "totalFees",   
        "pool"
    ]

    # Extract desired values and asign only desired dictionaries to clean_block list
    for key in keys:
        if key == "extras":
            for sub_key in extras:
                if sub_key == "pool":
                    pool_data = block_extras[sub_key]
                    pool_name = pool_data["name"]
                    clean_block.append({"pool_name": pool_name})
                else:
                    clean_block.append({sub_key: block_extras[sub_key]})
        else:        
            clean_block.append({key: block[key]})
    # Test what is returned
    print(clean_block)
    return clean_block


block = {
      "id": "0000000000000000000550783aea28c19a765840ee69f1f8f854a023f55ee319",
      "height": 729991,
      "version": 536895488,
      "timestamp": 1648824045,
      "bits": 386521239,
      "nonce": 3541117811,
      "difficulty": 28587155782195.14,
      "merkle_root": "5f45fe2dc980adfd28ec08ee97a235e65b046310e79e21f6c62dfc4fa01b3444",
      "tx_count": 2711,
      "size": 1531842,
      "weight": 3993519,
      "previousblockhash": "00000000000000000001eccd984f2dd8988c85bd4042425fb6bda5d25d93fd62",
      "mediantime": 1648821883,
      "extras": {
          "totalFees": 7317820,
          "medianFee": 6,
          "feeRange": [1, 4, 4, 6, 7, 10, 234],
          "reward": 632317820,
          "pool": {
              "id": 105,
              "name": "Binance Pool",
              "slug": "binancepool"
          },
          "avgFee": 2700,
          "avgFeeRate": 7,
          "coinbaseRaw": "0386230b1362696e616e63652f373832d8003303ad275122fabe6d6d6801fc8ec5270c7aeb937a23a219d47d12105b0ba9be097c2af52321be44dd85040000000000000079050100e2f20700",
          "coinbaseAddress": "1JvXhnHCi6XqcanvrZJ5s2Qiv4tsmm2UMy",
          "coinbaseAddresses": ["1JvXhnHCi6XqcanvrZJ5s2Qiv4tsmm2UMy"],
          "coinbaseSignature": "OP_DUP OP_HASH160 OP_PUSHBYTES_20 c499d0604392cc2051d7476056647d1c1bfc3f38 OP_EQUALVERIFY OP_CHECKSIG",
          "coinbaseSignatureAscii": "\u0003#\u000b\u0013binance/782Ø\u00003\u0003­'Q\"ú¾mmh\u0001üÅ'\fzëz#¢\u0019Ô}\u0012\u0010[\u000b©¾\t|*õ#!¾DÝ\u0004\u0000\u0000\u0000\u0000\u0000\u0000\u0000y\u0005\u0001\u0000âò\u0007\u0000",
          "avgTxSize": 564.89,
          "totalInputs": 7143,
          "totalOutputs": 5758,
          "totalOutputAmt": 199661543084,
          "medianFeeAmt": 1115,
          "feePercentiles": [113, 560, 763, 1115, 2008, 3553, 279500],
          "segwitTotalTxs": 2093,
          "segwitTotalSize": 1187865,
          "segwitTotalWeight": 2617719,
          "header": "0060002062fd935dd2a5bdb65f424240bd858c98d82d4f98cdec0100000000000000000044341ba04ffc2dc6f6219ee71063045be635a297ee08ec28fdad80c92dfe455fed0e476297d80917732b11d3",
          "utxoSetChange": -1385,
          "utxoSetSize": 80387028,
          "totalInputAmt": 199668860904,
          "virtualSize": 998379.75,
          "orphans": []
      }
  }

parse_block(block)
"""

"""
import requests
import sqlite3
import db

con = sqlite3.connect("database/blocks.db")
db = con.cursor()



print(db.execute("SELECT * FROM blocks").fetchall())
"""






# Generate qr code for bitcoin wallet address
"""
import qrcode
img = qrcode.make('Some data here')
type(img)  # qrcode.image.pil.PilImage
img.save("testing.png")

format
bitcoin:<address>[?amount=<amount>][?label=<label>][?message=<message>]
bitcoin:175tWpb8K1S7NmH4Zx6rewF9WQrcZv245W?amount=50&label=Luke-Jr&message=Donation%20for%20project%20xyz


import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('bitcoin:bc1qvgz5skmf9etdggqqharkvyf9weczefwumxw5yf?amount=0.00059&label=Molly&message=Happy%20Birth%20Day!')
qr.make(fit=True)

img = qr.make_image(back_color=(255, 165, 0), fill_color=(41, 39, 39))
img.save("testing.png")
"""


import os
import qrcode


my_dir = os.getcwd()
file = f"{my_dir}/static/images/address_qr.png" 

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('bitcoin:bc1qvgz5skmf9etdggqqharkvyf9weczefwumxw5yf?amount=0.00059&label=Molly&message=Happy%20Birth%20Day!')
qr.make(fit=True)

img = qr.make_image(back_color=(255, 165, 0), fill_color=(41, 39, 39))
img.save(file)



"""
import os

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
