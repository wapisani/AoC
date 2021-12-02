# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 18:37:36 2021

@author: wapisani
"""

import os
import numpy as np

directory = r'F:\Documents\Programming\AoC\2021'
os.chdir(directory)

with open('input_day2.txt','r') as handle:
    data = handle.readlines()
    
### Part 1 ###
directions = {'forward': 0, 'down': 0, 'up': 0}

for line in data:
    line = line.split(' ')
    direction = line[0]
    units = int(line[1])
    directions[direction] += units

x = directions['forward']
y = directions['down'] - directions['up']

print(f'The product of horizontal and vertical positions is {x*y}.')

### Part 2 ###
forward = 0
aim = 0
depth = 0
for line in data:
    line = line.split(' ')
    direction = line[0]
    value = int(line[1])
    if direction == 'down':
        aim += value
    elif direction == 'up':
        aim -= value
    elif direction == 'forward':
        forward += value
        depth += aim * value
        
print(f'The product of depth by horizontal position is {forward*depth}.')

