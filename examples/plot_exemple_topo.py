"""
"This" is my example-script
===========================

This example doesn't do much, it just makes a simple plot
"""
import matplotlib.pyplot as plt

from pytopomap.tools import read_tiff

from pytopomap.plot import plot_topo


url = r"https://raw.githubusercontent.com/Cykap/pytopomap/main/data/z.tif"

x, y, z = read_tiff(url)

axe = plot_topo(z, x, y)
plt.show()