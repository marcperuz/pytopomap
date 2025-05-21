r"""
plot_3d: plot_data_on_topo_3d
===========================

plot_data_on_topo_3d example:
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
# Little text.