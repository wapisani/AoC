#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 22:11:02 2020

@author: wapisani
"""

import os, math

os.chdir(r"/Users/wapisani/Documents/Programming/AoC/2020/Day3")

with open("input_Day3.txt",'r') as aoc_input:
    tree_map = [line.rstrip() for line in aoc_input]
    
# right 1, down 1, 61 trees
# right 3, down 1, 257 trees
# right 5, down 1, 64 trees
# right 7, down 1, 47 trees
# right 1, down 2, 38 trees
right = 1
down = 2

# The number of times going down is current 1 (but I'm guessing it will change)
# so the true number of rows is the length of the tree map divided by down
nrows = len(tree_map)/down
ncols = len(tree_map[0])
nrepeat = math.ceil(nrows/ncols)

expanded_tree_map = []
for index,tree_line in enumerate(tree_map):    
    for value in range(nrepeat):
        tree_line = tree_line + tree_line
    expanded_tree_map.append(tree_line)
    
    
tree_counter = 0
col_pos = 0
if down > 1:
    for tree_line in expanded_tree_map[down:-1:down]:
        col_pos += right
        if tree_line[col_pos] == '#':
            tree_counter += 1
else:
    for tree_line in expanded_tree_map[1:]:
        col_pos += right
        if tree_line[col_pos] == '#':
            tree_counter += 1

print(f"You will hit {tree_counter} trees with a slope of right {right}, down {down}.")
    
    
