# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 17:17:03 2022

@author: wapisani
"""

import os
import numpy as np

directory = r'F:\Documents\Programming\AoC\2022'
os.chdir(directory)

with open('input_day1.txt','r') as handle:
    data = handle.readlines()

elves = {}
elf_id = 1
for line in data:
    if line == '\n':
        elf_id += 1
        continue
    else:
        if elf_id not in elves:
            elves[elf_id] = {}
            elves[elf_id]['food'] = []
            elves[elf_id]['food'].append(int(line))
        else:
            elves[elf_id]['food'].append(int(line))


calories = []
elf_ids = list(range(1,len(elves)+1))
for key in elves:
    elf = elves[key]
    total_calories = sum(elf['food'])
    elf['total'] = total_calories
    calories.append(total_calories)

print(f"Part 1: The elf with the most calories is carrying {max(calories)} calories")

elf_calories = [] # list of tuples
for elf_id in elves:
    elf = elves[elf_id]
    elf_calories.append((elf_id,elf['total']))
    
sorted_elves = sorted(elf_calories,key=lambda x: x[1])

top_three_elves_calories = sorted_elves[-1][1] + sorted_elves[-2][1] + sorted_elves[-3][1]

print(f"Part 2: The total calories that the top three elves are carrying is {top_three_elves_calories}")
