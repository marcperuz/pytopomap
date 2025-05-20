Test function for plot_3D
=========================

Test for plot_topo_3d.

.. code-block:: python

	import matplotlib.pyplot as plt

	from pytopomap.tools import read_tiff

	from pytopomap.plot_3d import plot_topo_3D


	url = r"https://raw.githubusercontent.com/marcperuz/pytopomap/main/data/z.tif"

	x, y, z = read_tiff(url)

	plot_topo_3D(z, x, y, saving_path=r"./output", auto_open=True)

.. raw:: html
	:file: ..\\..\\examples\\output\\topography.html
	
Test for plot_data_on_topo_3D.
	
.. code-block:: python

	import matplotlib.pyplot as plt

	from pytopomap.tools import read_tiff

	from pytopomap.plot_3d import plot_data_on_topo_3D

	url_topo = r"https://raw.githubusercontent.com/marcperuz/pytopomap/main/data/z.tif"
	url_data = r"https://raw.githubusercontent.com/marcperuz/pytopomap/main/data/h_deposits.tif"

	x, y, z = read_tiff(url_topo)
	x, y, data = read_tiff(url_data)

	plot_data_on_topo_3D(x, y, z, data, saving_path=r"./output")
	
.. raw:: html
	:file: ..\\..\\examples\\output\\data_on_topography.html