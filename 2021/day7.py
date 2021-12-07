# -*- coding: utf-8 -*-
"""
@author: wapisani
"""

import os
import numpy as np
from collections import Counter

directory = r'F:\Documents\Programming\AoC\2021'
os.chdir(directory)

with open('input_day7.txt','r') as handle:
    data = handle.readlines()[0].split(',')
    data = [int(value) for value in data]

# with open('sample_day7.txt','r') as handle:
#     data = handle.readlines()[0].split(',')
#     data = [int(value) for value in data]

### Part 1 ###
crabs_pop_positions = Counter(data)

positions_to_try = []
for key in crabs_pop_positions:
    pos = crabs_pop_positions[key]
    if pos > 1:
        positions_to_try.append(key)

fuel_spent = []
for pos in positions_to_try:
        
    fuel_spent_value = 0
    for crab in data:
        fuel_spent_value += abs(crab - pos)
    fuel_spent.append(fuel_spent_value)
    
least_fuel_spent = fuel_spent[fuel_spent.index(min(fuel_spent))]
print(f'Part 1, least fuel spent is {least_fuel_spent}')    

### Part 2 ###


fuel_spent2 = []
for pos in range(max(data)+1):
    fuel_spent_value = 0
    for crab in data:
        distance = abs(crab - pos)
        fuel_spent_value += sum(range(distance+1))
    fuel_spent2.append(fuel_spent_value)
    
least_fuel_spent2 = min(fuel_spent2)
print(f'Part 2, least fuel spent is {least_fuel_spent2}')   


