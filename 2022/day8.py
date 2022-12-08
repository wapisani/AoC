# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 00:49:17 2022

@author: wapisani
"""
import os
import numpy as np

directory = r'F:\Documents\Programming\AoC\2022'
os.chdir(directory)

with open('input_day8.txt','r') as handle:
    data = handle.readlines()

# Part 1
nrows = len(data)
ncols = len(data[0].strip())
tree_heightmap = np.zeros((nrows,ncols))
for i,line in enumerate(data):
    line = [int(x) for x in line.strip()]
    tree_heightmap[i,:] = line

# Trees at the edge of the forest are visible, subtract corners
ntrees_visible =  2*nrows + 2*ncols - 4

# Iterate over the interior trees
for i in range(1,nrows-1):
    for j in range(1,ncols-1):
        tree = tree_heightmap[i,j]

        # Up
        if tree > np.max(tree_heightmap[:i,j]):
            ntrees_visible += 1
            continue
        
        # Down
        if tree > np.max(tree_heightmap[i+1:,j]):
            ntrees_visible += 1
            continue
        
        # Left
        if tree > np.max(tree_heightmap[i,:j]):
            ntrees_visible += 1
            continue
        
        # Right
        if tree > np.max(tree_heightmap[i,j+1:]):
            ntrees_visible += 1
            continue
        
print(f"There are {ntrees_visible} trees visible.")
        

# Part 2
scenic_scores = np.zeros((nrows,ncols))
for i in range(0,nrows):
    for j in range(0,ncols):
        vleft, vright, vup, vdown = 0,0,0,0
        tree = tree_heightmap[i,j]
            
        up = tree_heightmap[0:i,j]
        down = tree_heightmap[i+1:,j]
        left = tree_heightmap[i,0:j]
        right = tree_heightmap[i,j+1:]
        for t in up[::-1]:
            if t >= tree:
                vup += 1
                break
            else:
                vup += 1
                
        for t in down:
            if t >= tree:
                vdown += 1
                break
            else:
                vdown += 1
        
        for t in left[::-1]:
            if t >= tree:
                vleft += 1
                break
            else:
                vleft += 1
        
        for t in right:
            if t >= tree:
                vright += 1
                break
            else:
                vright += 1
        
        scenic_score = vleft * vright * vup * vdown
        scenic_scores[i,j] = scenic_score
        
print(f"The highest possible scenic score is {np.max(scenic_scores)}.")

