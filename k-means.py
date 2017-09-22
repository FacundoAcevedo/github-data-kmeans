#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 Facundo Acevedo <facevedo[AT]openmailbox[DOT]org>
#
# Distributed under terms of the GPLv3+ license.

"""

aplicanmos kmeans al dataset de github

"""

from sklearn.cluster import KMeans
import numpy as np
import csv

data = []

with open("facu-gh.csv", 'r', newline='') as csvfile:
        csv_reader = csv.reader(
            csvfile, delimiter=' ', quotechar='|',
            quoting=csv.QUOTE_MINIMAL)
        for linea in csv_reader:
            data.append([linea[0], linea[5], linea[6]])

            X = np.array(x for x in data)
            kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
