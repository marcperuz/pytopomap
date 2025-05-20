"""
plot: plot_topo
===========================

plot_topo example:
"""
from pytopomap.tools import read_tiff

from pytopomap.plot_3d import plot_topo_3D


url = r"https://raw.githubusercontent.com/marcperuz/pytopomap/main/data/z.tif"

x, y, z = read_tiff(url)

fig = plot_topo_3D(z, x, y, saving_path=r"./output", auto_open=True)
