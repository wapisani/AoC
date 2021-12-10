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
local_minima_locations = [] # for part 2
for row in range(n_rows):
    for col in range(n_cols):
        if row == 0: # top row
            if col == 0: # top-left element
                element = height_map[row,col]
                right = height_map[row,col+1]
                down = height_map[row+1,col]
                if element < right and element < down:
                    local_minima.append(element)
                    local_minima_locations.append((row,col))
                    
            elif col == n_cols-1: # far-right column
                element = height_map[row,col]
                left = height_map[row,col-1]
                down = height_map[row+1,col]
                if element < left and element < down:
                    local_minima.append(element)
                    local_minima_locations.append((row,col))
                    
            else: # anywhere in top row between far-left and far-right
                element = height_map[row,col]
                left = height_map[row,col-1]
                right = height_map[row,col+1]
                down = height_map[row+1,col]
                if element < left and element < right and element < down:
                    local_minima.append(element)
                    local_minima_locations.append((row,col))
                    
        elif row == n_rows-1: # bottom row
            if col == 0: # bottom-left element
                element = height_map[row,col]
                up = height_map[row-1,col]
                right = height_map[row,col+1]
                if element < up and element < right:
                    local_minima.append(element)
                    local_minima_locations.append((row,col))
                    
            elif col == n_cols-1: # bottom-right element
                element = height_map[row,col]
                up = height_map[row-1,col]
                left = height_map[row,col-1]
                if element < up and element < left:
                    local_minima.append(element)
                    local_minima_locations.append((row,col))
                    
            else: # anywhere in bottom row between left and right 
                element = height_map[row,col]
                up = height_map[row-1,col]
                left = height_map[row,col-1]
                right = height_map[row,col+1]
                if element < up and element < left and element < right:
                    local_minima.append(element)
                    local_minima_locations.append((row,col))
                    
        else: # anywhere inside the top and bottom rows
            if col == 0: # left col
                element = height_map[row,col]
                up = height_map[row-1,col]
                right = height_map[row,col+1]
                down = height_map[row+1,col]
                if element < up and element < right and element < down:
                    local_minima.append(element)
                    local_minima_locations.append((row,col))
                    
            elif col == n_cols-1: # right col
                element = height_map[row,col]
                up = height_map[row-1,col]
                left = height_map[row,col-1]
                down = height_map[row+1,col]
                if element < up and element < left and element < down:
                    local_minima.append(element)
                    local_minima_locations.append((row,col))
                    
            else: # anywhere inside the edges
                element = height_map[row,col]
                up = height_map[row-1,col]
                left = height_map[row,col-1]
                right = height_map[row,col+1]
                down = height_map[row+1,col]
                if element < up and element < left and element < right and element < down:
                    local_minima.append(element)
                    local_minima_locations.append((row,col))
                    
risk_levels = [minima+1 for minima in local_minima]
print(f'The sum of the risk levels of all the low points on the height map is {int(sum(risk_levels))}')

### Part 2 ###
def bfs(height_map,local_minima): # local_minima is tuple of (row,col) where the local minima is
    
    visited = []
    queue = [local_minima]
    n_rows,n_cols = height_map.shape
    while queue:
        
        node = queue.pop(0)
        row,col = node
        if node not in visited: # There may be a bug somewhere
            visited.append(node)
            neighbors = []
            if row == 0 and col == 0: # upper-left
                right = height_map[row,col+1]
                down = height_map[row+1,col]
                if right < 9:
                    neighbors.append((row,col+1))
                if down < 9:
                    neighbors.append((row+1,col))
            elif row == 0 and col == n_cols-1: # upper-right
                left = height_map[row,col-1]
                down = height_map[row+1,col]
                if left < 9:
                    neighbors.append((row,col-1))
                if down < 9:
                    neighbors.append((row+1,col))
            elif row == n_rows-1 and col == n_cols-1: # lower-right
                up = height_map[row-1,col]
                left = height_map[row,col-1]
                if left < 9:
                    neighbors.append((row,col-1))
                if up < 9:
                    neighbors.append((row-1,col))
            elif row == n_rows-1 and col == 0: # lower-left
                up = height_map[row-1,col]
                right = height_map[row,col+1]
                if up < 9:
                    neighbors.append((row-1,col))
                if right < 9:
                    neighbors.append((row,col+1))
            elif row == 0 and (col != 0 or col != n_cols-1): # top row
                left = height_map[row,col-1]
                right = height_map[row,col+1]
                down = height_map[row+1,col]
                if left < 9:
                    neighbors.append((row,col-1))
                if right < 9:
                    neighbors.append((row,col+1))
                if down < 9:
                    neighbors.append((row+1,col))
            elif row == n_rows-1 and (col != 0 or col != n_cols-1): # bottom-row
                left = height_map[row,col-1]
                right = height_map[row,col+1] 
                up = height_map[row-1,col]
                if left < 9:
                    neighbors.append((row,col-1))
                if right < 9:
                    neighbors.append((row,col+1))
                if up < 9:
                    neighbors.append((row-1,col))
            elif col == 0 and (row != 0 or row != n_rows-1): # left col, but not top or bottom
                right = height_map[row,col+1] 
                up = height_map[row-1,col]
                down = height_map[row+1,col]
                if right < 9:
                    neighbors.append((row,col+1))
                if down < 9:
                    neighbors.append((row+1,col))
                if up < 9:
                    neighbors.append((row-1,col))
            elif col == n_cols-1 and (row != 0 or row != n_rows-1): # right col, but not top or bottom
                up = height_map[row-1,col]
                down = height_map[row+1,col]
                left = height_map[row,col-1]
                if up < 9:
                    neighbors.append((row-1,col))
                if down < 9:
                    neighbors.append((row+1,col))
                if left < 9:
                    neighbors.append((row,col-1))
            else: # somewhere not on the edges
                up = height_map[row-1,col]
                down = height_map[row+1,col]
                left = height_map[row,col-1]
                right = height_map[row,col+1] 
                if up < 9:
                    neighbors.append((row-1,col))
                if down < 9:
                    neighbors.append((row+1,col))
                if left < 9:
                    neighbors.append((row,col-1))
                if right < 9:
                    neighbors.append((row,col+1))
                
            for neighbor in neighbors:
                queue.append(neighbor)
    return visited

basins = []
basin_sizes = []
for location in local_minima_locations:
    basin = bfs(height_map,location)
    basins.append(basin)
    basin_sizes.append(len(basin))
    
sorted_basins = sorted(basin_sizes,reverse=True)
basin1 = sorted_basins[0]
basin2 = sorted_basins[1]
basin3 = sorted_basins[2]
basin_product = basin1 * basin2 * basin3
for basin in sorted_basins[0:3]:
    print(f'Basin of size {basin}')

print(f'The product of the three largest basins is {basin_product}') 
    
