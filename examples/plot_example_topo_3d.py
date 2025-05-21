r"""
plot_3d: plot_topo_3d
===========================

plot_topo_3d example:
"""
from pytopomap.tools import read_tiff

from pytopomap.plot_3d import plot_topo_3D


url = r"https://raw.githubusercontent.com/marcperuz/pytopomap/main/data/z.tif"

x, y, z = read_tiff(url)

fig = plot_topo_3D(z, x, y)
fig

# %%
# Little text.