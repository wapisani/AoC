# -*- coding: utf-8 -*-
"""
@author: wapisani
"""

import os

directory = r'F:\Documents\Programming\AoC\2021'
os.chdir(directory)

with open('input_day6.txt','r') as handle:
    data = handle.readlines()[0].split(',')

# with open('sample_day6.txt','r') as handle:
#     data = handle.readlines()[0].split(',')
    
### Part 1 ###
fish = [int(value) for value in data]
days = 80
for day in range(days):
    new_fish_count = 0
    for index,timer in enumerate(fish):
        
        fish[index] -= 1
        if fish[index] < 0:
            fish[index] = 6
            new_fish_count += 1
        
    # Add new fish here
    for new_fish in range(new_fish_count):
        fish.append(8)

print(f'After {days} days, there are {len(fish)} fish.')

### Part 2 ###
