#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 16:16:39 2021

@author: peruzzetto
"""

import matplotlib
import pytest

import numpy as np

from pytopomap.plot import plot_topo

x = np.linspace(0, 5, 100)
y = np.linspace(0, 5, 100)


def z_hill(x, y):
    z = np.zeros((len(x), len(y)))
    for i in range(len(x)):
        for j in range(len(y)):
            z[i][j] = 1 - ((x[i] - 2.5)**2)/2 - ((y[j] - 2.5)**2)/4
    return z


def z_complex_topo(x, y):
    z = np.zeros((len(x), len(y)))
    for i in range(len(x)):
        for j in range(len(y)):
            z[i][j] = (np.sin(x[i]) * np.cos(y[j]) + 0.5 * np.sin(3 * x[i] + 1) * np.cos(2 * y[j] + 1) + 0.25 * np.sin(5 * x[i] + 2) * np.cos(4 * y[j] + 2))
    return z


@pytest.mark.parametrize("elevation", [
    np.zeros((100,100)),
    z_hill(x, y),
    z_complex_topo(x, y),
])


def test_topo(elevation):
    assert isinstance(plot_topo(elevation, x, y), matplotlib.axes._axes.Axes)


def test_topo_with_param():
    assert isinstance(plot_topo(z_hill(x, y), x, y, contour_step=2, nlevels=2, level_min=-1.5, step_contour_bold=0.5, label_contour=False, vert_exag=2, figsize=(12.1, 5.9), sea_level=-2.5, sea_color='blue', alpha=0.5, azdeg=20), matplotlib.axes._axes.Axes)
