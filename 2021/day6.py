# -*- coding: utf-8 -*-
"""
@author: wapisani
"""

import os
import numpy as np

directory = r'F:\Documents\Programming\AoC\2021'
os.chdir(directory)

with open('input_day6.txt','r') as handle:
    data = handle.readlines()[0].split(',')

# with open('sample_day6.txt','r') as handle:
#     data = handle.readlines()[0].split(',')
    
### Part 1 and 2 ###
# Part 1 80 days, Part 2 256 days
initial_fish = [int(value) for value in data]
days = 256
n = 9 # number of possible timer states
fish_count = np.zeros(n)
for fish in initial_fish:
    fish_count[fish] += 1

for day in range(days):
    new_fish_count = fish_count[0]
    for i in range(1,n):
        fish_count[i-1] = fish_count[i]
        
    fish_count[n-2-1] += new_fish_count
    fish_count[n-1] = new_fish_count

print(f'After {days} days, there are {int(np.sum(fish_count))} fish.')