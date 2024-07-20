import os

my_dir = os.getcwd()

with os.scandir(f"{my_dir}/static/images") as dir:
    for file in dir:
        if file.name.startswith('test') and file.is_file():
            print(file.name)




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