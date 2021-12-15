# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 22:58:59 2021

@author: wapisani
"""

import os
import numpy as np

directory = r'F:\Documents\Programming\AoC\2021'
# directory = r'/Users/wapisani/Documents/Programming/AoC/2021'
os.chdir(directory)

with open('input_day11.txt','r') as handle:
    data = [line.strip() for line in handle.readlines()]
   

# with open('sample_day11.txt','r') as handle:
#     data = [line.strip() for line in handle.readlines()]

def getAdjacentCells(cell,nrows,ncols):
    """
    Credit to https://github.com/statneutrino/AdventOfCode/blob/main/2021/python/day11.py
    for the logic of this function.

    Parameters
    ----------
    position : tuple
        (x,y)-coordinates of the cell to get adjacents of.

    Returns
    -------
    Set of (x,y)-coordinates of adjacent cells to cell

    """
    
    x,y = cell
    adjacentCells = set()
    
    if x != 0:
        adjacentCells.add((x-1,y)) # cell above
    if x != nrows - 1:
        adjacentCells.add((x+1,y)) # cell below
    if y != 0:
        adjacentCells.add((x,y-1)) # cell left
    if y != ncols - 1:
        adjacentCells.add((x,y+1)) # cell right
    if x != 0 and y != 0:
        adjacentCells.add((x-1,y-1)) # cell upper-left
    if x != 0 and y != ncols - 1:
        adjacentCells.add((x-1,y+1)) # cell upper-right
    if x != nrows - 1 and y != 0:
        adjacentCells.add((x+1,y-1)) # cell below-left
    if x != nrows - 1 and y != ncols - 1:
        adjacentCells.add((x+1,y+1)) # cell below-right
    return adjacentCells
    
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
    # Now get the flash locations into a usable format
    x = [value for value in flash_locs[0]]
    y = [value for value in flash_locs[1]]
    xy = []
    for i,value in enumerate(x):
        xy.append((value,y[i]))
        
    n_flashes += len(xy) # Get number of flashes for those that have flashed
    
    for flashed in xy:
        
        adjacentCells = getAdjacentCells(flashed, nrows, ncols)
        for cell in adjacentCells:
            i,j = cell
            energy_grid[i,j] += 1
            e = energy_grid[i,j]
            if e == 10:
                n_flashes += 1 # This should only count the number of adjacent cells that flash
                xy.append((i,j))
    
    for flashed in xy:
        i,j = flashed
        energy_grid[i,j] = 0 # reset
    flashes_list.append(n_flashes)
    
print(f'In 100 steps, there were {sum(flashes_list)} flashes.')