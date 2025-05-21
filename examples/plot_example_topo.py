"""
Plot topgraphy
===========================

Here is an example to display a topography using plot_topo from the plot module.
"""
import matplotlib.pyplot as plt

from pytopomap.tools import read_tiff

from pytopomap.plot import plot_topo


url = r"https://raw.githubusercontent.com/marcperuz/pytopomap/main/data/z.tif"

x, y, z = read_tiff(url)

axe = plot_topo(z, x, y)

plt.show()

# %%
# It is possible to add many parameters to modify the display.

axe = plot_topo(z, x, y, contour_step=10., vert_exag=1.5, sea_color='blue', sea_level=1, azdeg=180, altdeg=25)

plt.show()