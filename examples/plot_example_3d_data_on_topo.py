r"""
3D plot data on topography
===========================

Here is an example to display data on 3D topography using plot_data_on_topo_3D from the plot_3d module.
"""
from pytopomap.tools import read_tiff

from pytopomap.plot_3d import plot_data_on_topo_3D

url_topo = r"https://raw.githubusercontent.com/marcperuz/pytopomap/main/data/z.tif"
url_data = r"https://raw.githubusercontent.com/marcperuz/pytopomap/main/data/h_deposits.tif"

x, y, z = read_tiff(url_topo)
x, y, data = read_tiff(url_data)

fig = plot_data_on_topo_3D(x, y, z, data)
fig

# %%
# It is possible to add many parameters to modify the display.

fig = plot_data_on_topo_3D(x, y, z, data, light_source=[90, 60], minval=15, maxval=100)
fig