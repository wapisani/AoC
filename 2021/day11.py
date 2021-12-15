# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 22:58:59 2021

@author: wapisani
"""

import os
import numpy as np

# directory = r'F:\Documents\Programming\AoC\2021'
directory = r'/Users/wapisani/Documents/Programming/AoC/2021'
os.chdir(directory)

# with open('input_day11.txt','r') as handle:
#     data = [line.strip() for line in handle.readlines()]
   

with open('sample_day11.txt','r') as handle:
    data = [line.strip() for line in handle.readlines()]

def bfs(flash_rows,flash_cols): # flashed_loc is a li is tuple of (row,col) where the local minima is
    queue = []
    for index,row in enumerate(flash_rows):
        col = flash_cols[index]
        queue.append((row,col))
    visited = []
    n_flashes = 0
    flashed = []
    
    n_rows,n_cols = energy_grid.shape
    while queue:
        
        node = queue.pop(0)
        row,col = node
        
        
        if energy_grid[row,col] == 10:
            n_flashes += 1
            flashed.append((row,col))
        
        if node not in visited: 
            
            visited.append(node)
            neighbors = []
            if row == 0 and col == 0: # upper-left
                right = (row,col+1)
                down = (row,col+1)
                energy_grid[right] += 1
                energy_grid[down] += 1
                righte = energy_grid[row,col+1]
                downe = energy_grid[row+1,col]
                if righte == 10:
                    neighbors.append(right)
                    
                if downe == 10:
                    neighbors.append(down)
                    
            elif row == 0 and col == n_cols-1: # upper-right
                left = (row,col-1)
                down = (row+1,col)
                energy_grid[left] += 1
                energy_grid[down] += 1
                lefte = energy_grid[left]
                downe = energy_grid[down]
                if lefte == 10:
                    neighbors.append(left)
                    
                if downe == 10:
                    neighbors.append(down)
                    
            elif row == n_rows-1 and col == n_cols-1: # lower-right
                up = (row-1,col)
                left = (row,col-1)
                energy_grid[up] += 1
                energy_grid[left] += 1
                upe = energy_grid[up]
                lefte = energy_grid[left]
                if lefte == 10:
                    neighbors.append(left)
                    
                if upe == 10:
                    neighbors.append(up)
                    
            elif row == n_rows-1 and col == 0: # lower-left
                up = (row-1,col)
                right = (row,col+1)
                energy_grid[up] += 1
                energy_grid[right] += 1
                upe = energy_grid[up]
                righte = energy_grid[right]
                if upe == 10:
                    neighbors.append(up)
                if righte == 10:
                    neighbors.append(right)
                    
            elif row == 0 and (col != 0 or col != n_cols-1): # top row
                left = (row,col-1)
                right = (row,col+1)
                down = (row+1,col)
                energy_grid[left] += 1
                energy_grid[right] += 1
                energy_grid[down] += 1
                lefte = energy_grid[left]
                righte = energy_grid[right]
                downe = energy_grid[down]
                if lefte == 10:
                    neighbors.append(left)
                if righte == 10:
                    neighbors.append(right)
                if downe == 10:
                    neighbors.append(down)
            elif row == n_rows-1 and (col != 0 or col != n_cols-1): # bottom-row
                left = (row,col-1)
                right = (row,col+1)
                up = (row-1,col)
                energy_grid[left] += 1
                energy_grid[right] += 1
                energy_grid[up] += 1
                lefte = energy_grid[left]
                righte = energy_grid[right] 
                upe = energy_grid[up]
                if lefte == 10:
                    neighbors.append(left)
                if righte == 10:
                    neighbors.append(right)
                if upe == 10:
                    neighbors.append(up)
                    
            elif col == 0 and (row != 0 or row != n_rows-1): # left col, but not top or bottom
                right = (row,col+1)
                up = (row-1,col)
                down = (row+1,col)
                up_right = (row-1,col+1)
                down_right = (row+1,col+1)
                energy_grid[right] += 1
                energy_grid[down] += 1
                energy_grid[up_right] += 1
                energy_grid[down_right] += 1
                righte = energy_grid[right] 
                upe = energy_grid[up]
                downe = energy_grid[down]
                up_righte = energy_grid[up_right]
                down_righte = energy_grid[down_right]
                if righte == 10:
                    neighbors.append(right)
                if downe == 10:
                    neighbors.append(down)
                if upe == 10:
                    neighbors.append(up)
                if up_righte == 10:
                    neighbors.append(up_right)
                if down_righte == 10:
                    neighbors.append(down_right)
                    
            elif col == n_cols-1 and (row != 0 or row != n_rows-1): # right col, but not top or bottom 
                up = (row-1,col)
                down = (row+1,col)
                left = (row,col-1)
                up_left = (row-1,col-1)
                down_left = (row+1,col-1)
                energy_grid[up] += 1
                energy_grid[down] += 1
                energy_grid[left] += 1
                energy_grid[up_left] += 1
                energy_grid[down_left] += 1
                upe = energy_grid[up]
                downe = energy_grid[down]
                lefte = energy_grid[left]
                up_lefte = energy_grid[up_left]
                down_lefte = energy_grid[down_left]
                if upe == 10:
                    neighbors.append(up)
                if downe == 10:
                    neighbors.append(down)
                if lefte == 10:
                    neighbors.append(left)
                if up_lefte == 10:
                    neighbors.append(up_left)
                if down_lefte == 10:
                    neighbors.append(down_left)
                    
            else: # somewhere not on the edges
                up = (row-1,col)
                down = (row+1,col)
                left = (row,col-1)
                right = (row,col+1)
                up_left = (row-1,col-1)
                up_right = (row-1,col+1)
                down_left = (row+1,col-1)
                down_right = (row+1,col+1)
                directions = [up,down,left,right,up_left,up_right,
                              down_left,down_right]
                for direction in directions:
                    energy_grid[direction] += 1
                    
                upe = energy_grid[up]
                downe = energy_grid[down]
                lefte = energy_grid[left]
                righte = energy_grid[right] 
                up_righte = energy_grid[up_right]
                up_lefte = energy_grid[up_left]
                down_righte = energy_grid[down_right]
                down_lefte = energy_grid[down_left]
                if upe == 10:
                    neighbors.append(up)
                if downe == 10:
                    neighbors.append(down)
                if lefte == 10:
                    neighbors.append(left)
                if righte == 10:
                    neighbors.append(right)
                if up_righte == 10:
                    neighbors.append(up_right)
                if up_lefte == 10:
                    neighbors.append(up_left)
                if down_righte == 10:
                    neighbors.append(down_right)
                if down_lefte == 10:
                    neighbors.append(down_left)
                
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
    energy_grid += 1 # increase energy of all octopi 1
    flash_locs = np.where(energy_grid == 10)
    if len(flash_locs[0]) > 0:
        flash_rows = [row for row in flash_locs[0]]
        flash_cols = [col for col in flash_locs[1]]
        flashed,nflash = bfs(flash_rows,flash_cols)
        n_flashes += nflash
        flash_locs = np.where(energy_grid >= 10)
        energy_grid[flash_locs]
        flashes_list.append(n_flashes)
        
print(f'In 100 steps, there were {sum(flashes_list)} flashes.')