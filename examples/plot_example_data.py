r"""
plot: plot_imshow
===========================
Here is an example of plot_imshow:
"""
import matplotlib.pyplot as plt

from pytopomap.tools import read_tiff

from pytopomap.plot import plot_imshow


url = r"https://raw.githubusercontent.com/marcperuz/pytopomap/main/data/h_deposits.tif"

x, y, data = read_tiff(url)

axe = plot_imshow(x, y, data)

plt.show()

# %%
# Little text.