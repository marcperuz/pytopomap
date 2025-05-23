"""
Plot data on topography
===========================

Here is an example to display data on topography using plot_data_on_topo from the plot module.
"""
import matplotlib.pyplot as plt

from pytopomap.tools import read_tiff

from pytopomap.plot import plot_data_on_topo

url_topo = r"https://raw.githubusercontent.com/marcperuz/pytopomap/main/data/z.tif"
url_data = r"https://raw.githubusercontent.com/marcperuz/pytopomap/main/data/h_deposits.tif"

x, y, z = read_tiff(url_topo)
x, y, data = read_tiff(url_data)

axe = plot_data_on_topo(x, y, z, data, minval_abs=0.1)

plt.show()

# %%
# It is possible to add many parameters to modify the display.

axe = plot_data_on_topo(x, y, z, data, minval=10, maxval=100,  cmap_intervals=[10, 50, 100])

plt.show()