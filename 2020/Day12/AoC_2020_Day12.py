#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 23:31:55 2020

@author: wapisani

https://adventofcode.com/2020/day/12#part2
"""

import os

os.chdir(r"F:\Documents\Programming\AoC\2020\Day12")

with open("input_Day12.txt",'r') as aoc_input:
    directions = aoc_input.read().split('\n')
    
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
print(f"In part 1, the Manhattan distance is {manhattan_dist}")

# I can use a rotation matrix for the rotation of the way point
# about the ship.
# https://en.wikipedia.org/wiki/Transformation_matrix#Rotation
# The waypoint moves relative to the ship
# The waypoint will have its own coordinates perhaps as a two-element numpy array for easy matrix multiplication
# The ship will have its own coordinates as a numpy array
# The rotation may be tricky, it might be easier to write out a test scenario on paper
# I will also need a set of coordinates showing the distance from the waypoint to the ship
import numpy as np
waypoint_coords = np.array([[10],[1]]) # East, North. E is +, N is +
wp_rel2_ship = np.array([[10],[1]])
ship_coords = np.array([[0],[0]])

for direction in directions:
    if direction == '':
        continue
    action = direction[0]
    value = int(direction[1:])
    
    if action == 'N':
        waypoint_coords[1,0] += value
        wp_rel2_ship = waypoint_coords - ship_coords
    elif action == 'S':
        waypoint_coords[1,0] -= value
        wp_rel2_ship = waypoint_coords - ship_coords
    elif action == 'E':
        waypoint_coords[0,0] += value
        wp_rel2_ship = waypoint_coords - ship_coords
    elif action == 'W':
        waypoint_coords[0,0] -= value
        wp_rel2_ship = waypoint_coords - ship_coords
    elif action == 'L': # counter-clockwise rotation
        angle = value*np.pi/180 # angle in radians
        rotation_matrix = np.array([[np.cos(angle),-1*np.sin(angle)],\
                             [np.sin(angle),np.cos(angle)]])
        wp_rel2_ship = np.matmul(rotation_matrix,wp_rel2_ship)
        waypoint_coords = ship_coords + wp_rel2_ship
    elif action == 'R': # clockwise rotation
        angle = value*np.pi/180
        rotation_matrix = np.array([[np.cos(angle),np.sin(angle)],\
                                    [-1*np.sin(angle),np.cos(angle)]])
        wp_rel2_ship = np.matmul(rotation_matrix,wp_rel2_ship)
        waypoint_coords = ship_coords + wp_rel2_ship
    elif action == 'F':
        ship_coords = ship_coords + wp_rel2_ship * value
        waypoint_coords = waypoint_coords + wp_rel2_ship * value

manhattan_dist_pt2 = abs(ship_coords[0,0]) + abs(ship_coords[1,0])
print(f"In part 2, the Manhattan distance is {manhattan_dist_pt2}")
        
        
        
    
    
    
    
    
    
    
    
