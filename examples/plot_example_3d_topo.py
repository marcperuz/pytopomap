r"""
3D plot topography
===========================

Here is an example to display 3D topography using plot_topo_3D from the plot_3d module.
"""
from pytopomap.tools import read_tiff

from pytopomap.plot_3d import plot_topo_3D


url = r"https://raw.githubusercontent.com/marcperuz/pytopomap/main/data/z.tif"

x, y, z = read_tiff(url)

fig = plot_topo_3D(z, x, y)
fig

# %%
# It is possible to add many parameters to modify the display.

fig = plot_topo_3D(z, x, y, light_source=[180, 15], add_walls=False, add_floor=False)
fig