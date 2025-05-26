r"""
Plot data
===========================

This example demonstrates how to display data using plot_imshow from the plot module.
"""
import matplotlib.pyplot as plt

from pytopomap.tools import read_tiff
from pytopomap.plot import plot_imshow

# Load data from a GeoTIFF file (available on github)
url = r"https://raw.githubusercontent.com/marcperuz/pytopomap/main/data/h_deposits.tif"
x, y, data = read_tiff(url)

# Basic imshow usage.
axe = plot_imshow(x, y, data)

plt.show()

# %%
# Customized display with advanced parameters
# -------------------------------------------
# You can customize the colormap, display range, and value segmentation. Example with:
# 
# - 'viridis' colormap
# 
# - Display only values between 20 and 100
# 
# - Discrete color intervals

axe = plot_imshow(
    x,
    y,
    data,
    cmap="viridis",
    minval=20,
    maxval=100,
    cmap_intervals=[20, 40, 60, 80, 100]
)

plt.show()

# %%
# You can also display only unique values (e.g., class labels or categories)
# This enables a discrete colorbar with labeled ticks.

# Simulated categorical values:
data_cat = data.copy()
data_cat[(data_cat >= 0) & (data_cat < 30)] = 1
data_cat[(data_cat >= 30) & (data_cat < 60)] = 2
data_cat[(data_cat >= 60)] = 3

axe = plot_imshow(
    x,
    y,
    data_cat,
    cmap="tab10",
    unique_values=True
)

plt.show()

# %%
# You can remove low-magnitude values using `minval_abs`
# Useful for cleaning noisy data near zero for instance.

axe = plot_imshow(
    x,
    y,
    data,
    cmap="plasma",
    minval_abs=10
)

plt.show()
