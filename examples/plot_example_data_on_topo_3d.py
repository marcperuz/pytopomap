"""
plot: plot_data_on_topo
===========================

plot_data_on_topo example:
"""
import matplotlib.pyplot as plt

from pytopomap.tools import read_tiff

from pytopomap.plot_3d import plot_data_on_topo_3D

url_topo = r"https://raw.githubusercontent.com/marcperuz/pytopomap/main/data/z.tif"
url_data = r"https://raw.githubusercontent.com/marcperuz/pytopomap/main/data/h_deposits.tif"

x, y, z = read_tiff(url_topo)
x, y, data = read_tiff(url_data)

plot_data_on_topo_3D(x, y, z, data, saving_path=r"./output")