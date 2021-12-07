# -*- coding: utf-8 -*-
"""
@author: wapisani
"""

import os
directory = r'F:\Documents\Programming\AoC\2021'
os.chdir(directory)

with open('input_day7.txt','r') as handle:
    data = [int(value) for value in handle.readlines()[0].split(',')]

# with open('sample_day7.txt','r') as handle:
#     data = [int(value) for value in handle.readlines()[0].split(',')]
fuel_spent_part1 = []
fuel_spent_part2 = []
for pos in range(max(data)+1):
    fuel_spent1 = 0
    fuel_spent2 = 0
    for crab in data:
        distance = abs(crab - pos)
        fuel_spent1 += distance
        fuel_spent2 += distance * (distance+1)/2
        
    fuel_spent_part1.append(fuel_spent1)   
    fuel_spent_part2.append(fuel_spent2)
print(f'Part 1, least fuel spent is {min(fuel_spent_part1)}')    
print(f'Part 2, least fuel spent is {int(min(fuel_spent_part2))}')  