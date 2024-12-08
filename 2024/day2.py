#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 00:15:32 2024

@author: wapisani
"""


import os, re
from operator import itemgetter
import numpy as np

directory = r'/home/wapisani/Documents/Programming/AoC/2024'
os.chdir(directory)

with open('input_day2.txt','r') as handle:
    data = handle.readlines()
    
# example data
# data = """7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9""".split('\n')

safe = 0

list_data = []
for line in data:
    list_data.append(np.asarray([int(x) for x in line.strip().split()]))

def safety_check(row):
    # Levels must be either all increasing or all decreasing
    if np.all(row > 0) == True or np.all(row < 0) == True:
        # Levels must have at least a difference of 1 and no more than 3
        if np.all(np.abs(row)>=1) == True and np.all(np.abs(row)<=3) == True:
            return True
    return False

safe_indices = []
for i,line in enumerate(list_data):
    row = np.diff(line)
    if safety_check(row):
        safe += 1
        safe_indices.append(i)
  
print("Part 1")
print(f"There are {safe} safe reports")  

part2_data = []
for i,line in enumerate(list_data):
    if i not in safe_indices:
        part2_data.append(line)
        
diff_list = [np.diff(row) for row in part2_data]

# Bruteforce method
for line in part2_data:
    for i in range(len(line)):
        new_line = np.delete(line,i)
        diff_line = np.diff(new_line)
        if safety_check(diff_line):
            safe += 1
            break
        
print("\nPart 2")
print(f"There are now {safe} safe reports")