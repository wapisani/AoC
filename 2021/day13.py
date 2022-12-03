# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 14:06:51 2022

@author: wapisani
"""

import os
import numpy as np

directory = r'F:\Documents\Programming\AoC\2021'
os.chdir(directory)

with open('input_day13.txt','r') as handle:
    data = handle.readlines()

x_values, y_values = [], []
folds = [] # List of lists [x/y,/row/col]
for index,line in enumerate(data):
    if line == '\n':
        fold_lines = data[index+1:]
        break
    else:
        line = line.strip().split(',')
        y_values.append(int(line[0]))
        x_values.append(int(line[1]))

xhi = max(x_values)
yhi = max(y_values)

for fold in fold_lines:
    fold = fold.strip().split(' ')[-1]
    x_y,row_col = fold.split('=')
    folds.append([x_y,int(row_col)])

paper = np.zeros((xhi+1,yhi+1))
for index,x in enumerate(x_values):
    y = y_values[index]
    paper[x,y] = 1
    
paper = np.array(paper,dtype=bool)

for fold in folds:
    if fold[0] == 'x':
        row = fold[1]
        half1 = paper[1:row,:]
        half2 = paper[row:,:]
        paper = half1 + half2
    else:
        col = fold[1]
        half1 = paper[:,1:col]
        half2 = paper[:,col:]
        paper = half1 + half2
    print(f'Number of dots after {fold}: {np.sum(paper)}')
