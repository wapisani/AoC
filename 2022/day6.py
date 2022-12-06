# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 17:10:18 2022

@author: wapisani
"""
import os
from collections import deque
directory = r'F:\Documents\Programming\AoC\2022'
os.chdir(directory)

with open('input_day6.txt','r') as handle:
    data = handle.readlines()

# Part 1
marker = deque()
for i,letter in enumerate(data[0].strip()):
    marker.append(letter)
    if len(marker) == 4:
        if len(set(marker)) == 4:
            print(f"{i+1} characters processed before the first start-of-packet marker was detected.")
        else:
            marker.popleft()
                
# Part 2
marker = deque()
for i,letter in enumerate(data[0].strip()):
    marker.append(letter)
    if len(marker) == 14:
        if len(set(marker)) == 14:
            print(f"{i+1} characters processed before the first start-of-message marker was detected.")
        else:
            marker.popleft()