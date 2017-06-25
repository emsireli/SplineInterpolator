# -*- coding: utf-8 -*-
"""
Python 3

This program reads csv files, sorts them and fits a spline curve.
"""

import csv

with open('data4spl.csv', newline='') as csvFileObj:
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        rawData = list(readerObj)

print(rawData)
        