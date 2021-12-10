# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 12:13:36 2021

@author: wapisani
"""

import os
import numpy as np
directory = r'F:\Documents\Programming\AoC\2021'
os.chdir(directory)

with open('input_day9.txt','r') as handle:
    data = [line.strip() for line in handle.readlines()]
   

# with open('sample_day9.txt','r') as handle:
#     data = [line.strip() for line in handle.readlines()]

# Initialize height map from input data
n_rows = len(data)
n_cols = len(data[0])
height_map = np.zeros((n_rows,n_cols))
for row,line in enumerate(data):
    for col,value in enumerate(line):
        height_map[row,col] = int(value)

local_minima = []
for row in range(n_rows):
    for col in range(n_cols):
        if row == 0: # top row
            if col == 0: # top-left element
                element = height_map[row,col]
                right = height_map[row,col+1]
                down = height_map[row+1,col]
                if element < right and element < down:
                    local_minima.append(element)
                    
            elif col == n_cols-1: # far-right column
                element = height_map[row,col]
                left = height_map[row,col-1]
                down = height_map[row+1,col]
                if element < left and element < down:
                    local_minima.append(element)
            
            else: # anywhere in top row between far-left and far-right
                element = height_map[row,col]
                left = height_map[row,col-1]
                right = height_map[row,col+1]
                down = height_map[row+1,col]
                if element < left and element < right and element < down:
                    local_minima.append(element)
        
        elif row == n_rows-1: # bottom row
            if col == 0: # bottom-left element
                element = height_map[row,col]
                up = height_map[row-1,col]
                right = height_map[row,col+1]
                if element < up and element < right:
                    local_minima.append(element)
                    
            elif col == n_cols-1: # bottom-right element
                element = height_map[row,col]
                up = height_map[row-1,col]
                left = height_map[row,col-1]
                if element < up and element < left:
                    local_minima.append(element)
                    
            else: # anywhere in bottom row between left and right 
                element = height_map[row,col]
                up = height_map[row-1,col]
                left = height_map[row,col-1]
                right = height_map[row,col+1]
                if element < up and element < left and element < right:
                    local_minima.append(element)
        else: # anywhere inside the top and bottom rows
            if col == 0: # left col
                element = height_map[row,col]
                up = height_map[row-1,col]
                right = height_map[row,col+1]
                down = height_map[row+1,col]
                if element < up and element < right and element < down:
                    local_minima.append(element)
            elif col == n_cols-1: # right col
                element = height_map[row,col]
                up = height_map[row-1,col]
                left = height_map[row,col-1]
                down = height_map[row+1,col]
                if element < up and element < left and element < down:
                    local_minima.append(element)
            else: # anywhere inside the edges
                element = height_map[row,col]
                up = height_map[row-1,col]
                left = height_map[row,col-1]
                right = height_map[row,col+1]
                down = height_map[row+1,col]
                if element < up and element < left and element < right and element < down:
                    local_minima.append(element)
risk_levels = [minima+1 for minima in local_minima]
print(f'The sum of the risk levels of all the low points on the height map is {int(sum(risk_levels))}')


