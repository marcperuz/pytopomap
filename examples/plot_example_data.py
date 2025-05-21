r"""
Plot data
===========================

Here is an example to display data using plot_imshow from the plot module.
"""
import matplotlib.pyplot as plt

from pytopomap.tools import read_tiff

from pytopomap.plot import plot_imshow


url = r"https://raw.githubusercontent.com/marcperuz/pytopomap/main/data/h_deposits.tif"

x, y, data = read_tiff(url)

axe = plot_imshow(x, y, data)

plt.show()

# %%
# It is possible to add many parameters to modify the display.

axe = plot_imshow(x, y, data, cmap="viridis", minval=20, maxval=100, cmap_intervals=[20, 40, 60, 80, 100])

plt.show()