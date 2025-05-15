#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 16:16:39 2021

@author: peruzzetto
"""

import matplotlib
import pytest

import numpy as np

from pytopomap.plot import plot_imshow

x = np.linspace(0, 5, 100)
y = np.linspace(0, 5, 100)


def data_hill(x, y):
    data = np.zeros((len(x), len(y)))
    for i in range(len(x)):
        for j in range(len(y)):
            data[i][j] = 1 - ((x[i] - 2.5)**2)/3 - ((y[j] - 2.5)**2)/0.5
    return data


def test_imshow():
    assert isinstance(plot_imshow(x, y, data_hill(x, y)), matplotlib.axes._axes.Axes)


def test_imshow_with_param():
    assert isinstance(plot_imshow(x, y, data_hill(x, y), figsize=(12.1, 4.6), cmap="viridis", minval=0.1, maxval=0.9, alpha=0.9, cmap_intervals=[0.2, 0.3, 0.4, 0.5, 0.6], plot_colorbar=False), matplotlib.axes._axes.Axes)
