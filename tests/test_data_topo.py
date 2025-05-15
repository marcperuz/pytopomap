#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 16:16:39 2021

@author: peruzzetto
"""

import matplotlib
import pytest

import numpy as np

from pytopomap.plot import plot_data_on_topo

x = np.linspace(0, 5, 100)
y = np.linspace(0, 5, 100)


def data_hill(x, y):
    data = np.zeros((len(x), len(y)))
    for i in range(len(x)):
        for j in range(len(y)):
            data[i][j] = 1 - ((x[i] - 2.5)**2)/3 - ((y[j] - 2.5)**2)/0.5
    return data


def z_hill(x, y):
    z = np.zeros((len(x), len(y)))
    for i in range(len(x)):
        for j in range(len(y)):
            z[i][j] = 1 - ((x[i] - 2.5)**2)/2 - ((y[j] - 2.5)**2)/4
    return z


def test_data_on_topo():
    assert isinstance(plot_data_on_topo(x, y, np.zeros((100,100)), data_hill(x, y)), matplotlib.axes._axes.Axes)


def test_data_on_topo_with_param():
    assert isinstance(plot_data_on_topo(x, y, z_hill(x, y), data_hill(x, y), figsize=(10, 10), cmap='viridis', minval=0.1, maxval=0.9, alpha=0.9, cmap_intervals=[0.2, 0.3, 0.4, 0.5, 0.6], plot_colorbar=False, topo_kwargs={"sea_level": -2.5, "sea_color": 'blue'}), matplotlib.axes._axes.Axes)
