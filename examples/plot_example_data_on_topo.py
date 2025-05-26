r"""
Plot data on topography
===========================

This example demonstrates how to display data on topography using plot_data_on_topo from the plot module.
"""
import matplotlib.pyplot as plt

from pytopomap.tools import read_tiff
from pytopomap.plot import plot_data_on_topo

# Load data from a GeoTIFF file (available on github)
url_topo = r"https://raw.githubusercontent.com/marcperuz/pytopomap/main/data/z.tif"
url_data = r"https://raw.githubusercontent.com/marcperuz/pytopomap/main/data/h_deposits.tif"
x, y, z = read_tiff(url_topo)
x, y, data = read_tiff(url_data)


# Basic usage: display data imshow on topography.
axe = plot_data_on_topo(x, y, z, data, minval_abs=0.1)

plt.show()


# %%
# Customized display with advanced parameters
# -------------------------------------------
# You can adjust many parameters of plot_topo and plot_imshow such as:
# 
# - 'minval', 'maxval' or 'cmap_intervals': control the colormap range
# 
# - 'alpha': transparency of the data layer
# 
# - 'minval_abs': threshold to mask small values
# 
# - 'topo_kwargs': settings for the underlying topography (e.g., shading, exaggeration)
# 
# - 'mask', 'alpha_mask', 'color_mask': to overlay a binary mask (e.g., invalid zones)
# 
# - 'xlims', 'ylims': to zoom on a specific area


axe = plot_data_on_topo(
    x, y, z, data,
    minval=10,
    maxval=100,
    cmap_intervals=[10, 50, 100],
)

plt.show()