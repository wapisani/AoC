# -*- coding: utf-8 -*-
"""
@author: wapisani
"""

import os
import numpy as np


directory = r'F:\Documents\Programming\AoC\2021'
os.chdir(directory)

with open('input_day5.txt','r') as handle:
    data = handle.readlines()
    data = [line.strip() for line in data]

# with open('sample_day5.txt','r') as handle:
#     data = handle.readlines()
#     data = [line.strip() for line in data]

### Part 1 ###

# Parse data
line_segments = [] # list of tuples (x1,y1,x2,y2)
for line in data:
    line = line.split(' -> ')
    x1, y1 = map(int,line[0].split(','))
    x2, y2 = map(int,line[1].split(','))
    if x1 == x2 or y1 == y2:
        if x1 > x2: # I assume later that x2 > x1 and y2 > y1, so make sure it's like that
            x1,x2 = x2,x1
        if y1 > y2:
            y1,y2 = y2,y1
        line_segments.append((x1,y1,x2,y2))

# Set up a matrix of zeroes then increment each cell where a line crosses
N = np.max(line_segments)+1
dot_diagram = np.zeros((N,N))

for line in line_segments:
    x1,y1,x2,y2 = line
    if x1 == x2:
        for y in range(y1,y2+1): # Stop is exclusive, so increment by 1 to include y2
            dot_diagram[x1,y] += 1
    elif y1 == y2:
        for x in range(x1,x2+1): # Stop is exclusive, so increment by 1 to include x2
            dot_diagram[x,y1] += 1
            
# Get all the cells where at least two lines overlap (cell has a value of at least 2)
cells = np.where(dot_diagram > 1)
print(f'At least two lines overlap at {len(cells[0])} points')

### Part 2 ###

# Parse data
line_segments = [] # list of tuples (x1,y1,x2,y2)
for line in data:
    line = line.split(' -> ')
    x1, y1 = map(int,line[0].split(','))
    x2, y2 = map(int,line[1].split(','))
    
    if x1 > x2: # I assume later that x2 > x1 and y2 > y1, so make sure it's like that
        if y1 == y2:
            x1,x2 = x2,x1
            
    if y1 > y2:
        if x1 == x2:
            y1,y2 = y2,y1
    line_segments.append((x1,y1,x2,y2))

# Set up a matrix of zeroes then increment each cell where a line crosses
N = np.max(line_segments)+1
dot_diagram = np.zeros((N,N))

for line in line_segments:
    x1,y1,x2,y2 = line
    
    if x1 == x2:
        for y in range(y1,y2+1): 
            dot_diagram[x1,y] += 1
    elif y1 == y2:
        for x in range(x1,x2+1): 
            dot_diagram[x,y1] += 1
    else:
        # Determine distance between points, 45 degree angle means the
        # distance will be the same for both x and y
        x = x1
        y = y1
        dist = abs(x2 - x1)
        
        # Now figure out which direction to step in for x and y
        if x1 > x2:
            delta_x = -1
        else:
            delta_x = 1
        
        if y1 > y2:
            delta_y = -1
        else:
            delta_y = 1
        
        for i in range(dist+1):
            dot_diagram[x,y] += 1
            x += delta_x
            y += delta_y
        
        
        
            
# Get all the cells where at least two lines overlap (cell has a value of at least 2)
cells = np.where(dot_diagram > 1)
print(f'At least two lines overlap at {len(cells[0])} points')


