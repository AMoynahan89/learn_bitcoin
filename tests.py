import matplotlib.pyplot as plt
import numpy as np
import requests


def usd(n):
    n = f"${n:,.2f}"
    return n

response = requests.get("https://mempool.space/api/v1/historical-price")
data = response.json()



times = [result["time"] for result in data["prices"]]
prices = [result["USD"] for result in data["prices"]]

fig, ax = plt.subplots()             # Create a figure containing a single Axes.
ax.plot(times, prices)               # Plot some data on the Axes.
plt.show()                           # Show the figure.

