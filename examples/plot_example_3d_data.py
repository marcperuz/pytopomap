r"""
3D plot data
===========================

Here is an example to display 3D data using plot_imshow_3D from the plot_3d module.
"""
from pytopomap.tools import read_tiff

from pytopomap.plot_3d import plot_imshow_3D


url = r"https://raw.githubusercontent.com/marcperuz/pytopomap/main/data/h_deposits.tif"

x, y, data = read_tiff(url)

fig = plot_imshow_3D(x, y, data)
fig

# %%
# It is possible to add many parameters to modify the display.

fig = plot_imshow_3D(x, y, data, minval=15, maxval=100)
fig