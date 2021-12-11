# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 22:58:59 2021

@author: wapisani
"""

import os
import numpy as np

directory = r'F:\Documents\Programming\AoC\2021'
os.chdir(directory)

# with open('input_day11.txt','r') as handle:
#     data = [line.strip() for line in handle.readlines()]
   

with open('sample_day11.txt','r') as handle:
    data = [line.strip() for line in handle.readlines()]

def bfs(flashed_loc): # local_minima is tuple of (row,col) where the local minima is
    
    visited = []
    n_flashes = 0
    flashed = []
    queue = [flashed_loc]
    n_rows,n_cols = energy_grid.shape
    while queue:
        
        node = queue.pop(0)
        row,col = node
        energy_grid[row,col] += 1
        
        if energy_grid[row,col] > 9:
            n_flashes += 1
            flashed.append((row,col))
        
        if node not in visited: 
            
            visited.append(node)
            neighbors = []
            if row == 0 and col == 0: # upper-left
                right = energy_grid[row,col+1]
                down = energy_grid[row+1,col]
                if right > 8:
                    neighbors.append((row,col+1))
                    
                if down > 8:
                    neighbors.append((row+1,col))
                    
            elif row == 0 and col == n_cols-1: # upper-right
                left = energy_grid[row,col-1]
                down = energy_grid[row+1,col]
                if left > 8:
                    neighbors.append((row,col-1))
                    
                    
                if down > 8:
                    neighbors.append((row+1,col))
            elif row == n_rows-1 and col == n_cols-1: # lower-right
                up = energy_grid[row-1,col]
                left = energy_grid[row,col-1]
                if left > 8:
                    neighbors.append((row,col-1))
                if up > 8:
                    neighbors.append((row-1,col))
            elif row == n_rows-1 and col == 0: # lower-left
                up = energy_grid[row-1,col]
                right = energy_grid[row,col+1]
                if up > 8:
                    neighbors.append((row-1,col))
                if right > 8:
                    neighbors.append((row,col+1))
            elif row == 0 and (col != 0 or col != n_cols-1): # top row
                left = energy_grid[row,col-1]
                right = energy_grid[row,col+1]
                down = energy_grid[row+1,col]
                if left > 8:
                    neighbors.append((row,col-1))
                if right > 8:
                    neighbors.append((row,col+1))
                if down > 8:
                    neighbors.append((row+1,col))
            elif row == n_rows-1 and (col != 0 or col != n_cols-1): # bottom-row
                left = energy_grid[row,col-1]
                right = energy_grid[row,col+1] 
                up = energy_grid[row-1,col]
                if left > 8:
                    neighbors.append((row,col-1))
                if right > 8:
                    neighbors.append((row,col+1))
                if up > 8:
                    neighbors.append((row-1,col))
            elif col == 0 and (row != 0 or row != n_rows-1): # left col, but not top or bottom
                right = energy_grid[row,col+1] 
                up = energy_grid[row-1,col]
                down = energy_grid[row+1,col]
                if right > 8:
                    neighbors.append((row,col+1))
                if down > 8:
                    neighbors.append((row+1,col))
                if up > 8:
                    neighbors.append((row-1,col))
            elif col == n_cols-1 and (row != 0 or row != n_rows-1): # right col, but not top or bottom
                up = energy_grid[row-1,col]
                down = energy_grid[row+1,col]
                left = energy_grid[row,col-1]
                if up > 8:
                    neighbors.append((row-1,col))
                if down > 8:
                    neighbors.append((row+1,col))
                if left > 8:
                    neighbors.append((row,col-1))
            else: # somewhere not on the edges
                up = energy_grid[row-1,col]
                down = energy_grid[row+1,col]
                left = energy_grid[row,col-1]
                right = energy_grid[row,col+1] 
                if up > 8:
                    neighbors.append((row-1,col))
                if down > 8:
                    neighbors.append((row+1,col))
                if left > 8:
                    neighbors.append((row,col-1))
                if right > 8:
                    neighbors.append((row,col+1))
                
            for neighbor in neighbors:
                queue.append(neighbor)
    return flashed, n_flashes

nrows = len(data)
ncols = len(data[0])
energy_grid = np.zeros((nrows,ncols))
for i,line in enumerate(data):
    for j,char in enumerate(line):
        energy_grid[i,j] = int(char)

flashes_list = [] # count of flashes per step    
for step in range(100):
    n_flashes = 0
    for row in range(nrows):
        for col in range(ncols):
            flashed, nflash = bfs((row,col))
            n_flashes += nflash
            for flash in flashed:
                r,c = flash
                energy_grid[r,c] = 0
            
                # call bfs here, return number of flashes
                # Write a function called flash that will 
                # increase the energy levels of the 
                # 8 adjacent squares by 1 and then check 
                # for any new octopi that can flash. Change
                # the energy levels of any flashed to 0 before
                # moving on. Maybe bfs would be useful?
    flashes_list.append(n_flashes)
print(f'In 100 steps, there were {sum(flashes_list)} flashes.')