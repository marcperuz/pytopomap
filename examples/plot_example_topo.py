"""
plot: plot_topo
===========================

plot_topo example:
"""
import matplotlib.pyplot as plt

from pytopomap.tools import read_tiff

from pytopomap.plot import plot_topo


url = r"https://raw.githubusercontent.com/marcperuz/pytopomap/main/data/z.tif"

x, y, z = read_tiff(url)

axe = plot_topo(z, x, y)

plt.show()

# %%
# Little text.