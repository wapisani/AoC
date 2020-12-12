#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 23:31:55 2020

@author: wapisani
"""


import os

os.chdir(r"/home/wapisani/Documents/Programming/AoC/2020/Day12")

with open("input_Day12.txt",'r') as aoc_input:
    directions = aoc_input.read().split('\n')
    

    # Action N means to move north by the given value.
    # Action S means to move south by the given value.
    # Action E means to move east by the given value.
    # Action W means to move west by the given value.
    # Action L means to turn left the given number of degrees.
    # Action R means to turn right the given number of degrees.
    # Action F means to move forward by the given value in the direction the ship is currently facing.
# The ship starts by facing east. Only the L and R actions change the direction the ship is facing. (That is, if the ship is facing east and the next instruction is N10, the ship would move north 10 units, but would still move east if the following action were F.)

# At the end of these instructions, the ship's Manhattan distance (sum of the absolute values of its east/west position and its north/south position) from its starting position is 17 + 8 = 25.

# Figure out where the navigation instructions lead. What is the Manhattan distance between that location and the ship's starting position?

dir_facing = 'E' # Ship starts by facing east
west_east_coord = 0
north_south_coord = 0

# East will be positive, north will be positive
for direction in directions:
    if direction == '':
        continue
    action = direction[0]
    value = int(direction[1:])
    
    if action == 'F':
        if dir_facing == 'E':
            west_east_coord += value
        elif dir_facing == 'W':
            west_east_coord -= value
        elif dir_facing == 'N':
            north_south_coord += value
        elif dir_facing == 'S':
            north_south_coord -= value
            
    if action == 'L':
        if value == 90:
            if dir_facing == 'E':
                dir_facing = 'N'
            elif dir_facing == 'N':
                dir_facing = 'W'
            elif dir_facing == 'W':
                dir_facing = 'S'
            elif dir_facing == 'S':
                dir_facing = 'E'
        elif value == 180:
            if dir_facing == 'E':
                dir_facing = 'W'
            elif dir_facing == 'W':
                dir_facing = 'E'
            elif dir_facing == 'N':
                dir_facing = 'S'
            elif dir_facing == 'S':
                dir_facing = 'N'
        elif value == 270:
            if dir_facing == 'E':
                dir_facing = 'S'
            elif dir_facing == 'N':
                dir_facing = 'E'
            elif dir_facing == 'W':
                dir_facing = 'N'
            elif dir_facing == 'S':
                dir_facing = 'W'
    elif action == 'R':
        if value == 90:
            if dir_facing == 'E':
                dir_facing = 'S'
            elif dir_facing == 'S':
                dir_facing = 'W'
            elif dir_facing == 'W':
                dir_facing = 'N'
            elif dir_facing == 'N':
                dir_facing = 'E'
        elif value == 180:
            if dir_facing == 'E':
                dir_facing = 'W'
            elif dir_facing == 'W':
                dir_facing = 'E'
            elif dir_facing == 'N':
                dir_facing = 'S'
            elif dir_facing == 'S':
                dir_facing = 'N'
        elif value == 270:
            if dir_facing == 'E':
                dir_facing = 'N'
            elif dir_facing == 'S':
                dir_facing = 'E'
            elif dir_facing == 'W':
                dir_facing = 'S'
            elif dir_facing == 'N':
                dir_facing = 'W'
    if action == 'N':
        north_south_coord += value
    elif action == 'S':
        north_south_coord -= value
    elif action == 'E':
        west_east_coord += value
    elif action == 'W':
        west_east_coord -= value
        
manhattan_dist = abs(north_south_coord) + abs(west_east_coord)
print(f"The Manhattan distance is {manhattan_dist}")