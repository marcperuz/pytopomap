#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 16:16:39 2021

@author: peruzzetto
"""

import os

import numpy as np

from pytopomap.plot import plot_maps

x = np.linspace(0, 5, 100)
y = np.linspace(0, 5, 100)

temporary_folder = r".\\temp"
os.mkdir(temporary_folder)


def data_hill_1(x, y):
    data = np.zeros((len(x), len(y)))
    for i in range(len(x)):
        for j in range(len(y)):
            data[i][j] = 1 - ((x[i] - 2.5)**2)/3 - ((y[j] - 2.5)**2)/0.5
    return data


def data_hill_2(x, y):
    data = np.zeros((len(x), len(y)))
    for i in range(len(x)):
        for j in range(len(y)):
            data[i][j] = 1 - ((x[i] - 2.5)**2)/3 - ((y[j] - 2.5)**2)/0.5
    return data


def z_hill(x, y):
    z = np.zeros((len(x), len(y)))
    for i in range(len(x)):
        for j in range(len(y)):
            z[i][j] = 1 - ((x[i] - 2.5)**2)/5 - ((y[j] - 2.5)**2)/5
    return z


def test_maps():
    plot_maps(x, y, z_hill(x, y), np.stack((data_hill_1(x, y), data_hill_2(x, y)), axis=-1), np.array([0.1, 0.2]), 'Test', temporary_folder)
    assert len(os.listdir(temporary_folder)) == 2
    os.remove(os.path.join(temporary_folder, "Test_0000.png"))
    os.remove(os.path.join(temporary_folder, "Test_0001.png"))
    os.rmdir(temporary_folder)
