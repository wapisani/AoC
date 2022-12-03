# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 12:47:43 2022

@author: wapisani
"""

import os, string

directory = r'F:\Documents\Programming\AoC\2022'
os.chdir(directory)

with open('input_day3.txt','r') as handle:
    data = handle.readlines()
    
# Part 1
alphabet = list(string.ascii_lowercase+string.ascii_uppercase)
priority_lookup = {letter: index+1 for index,letter in enumerate(alphabet)}
priorities = []
for rucksack in data:
    rucksack = rucksack.strip()
    pocket1 = set(rucksack[0:len(rucksack)//2])
    pocket2 = set(rucksack[len(rucksack)//2:])
    
    items_in_both_pockets = list(pocket1.intersection(pocket2))
            
    p = 0 # Priority
    for item in items_in_both_pockets:
        p += priority_lookup[item]
    
    priorities.append(p)
    
print(f'Part 1: The sum of the priorities of items that appear in both compartments is {sum(priorities)}.')
    
# Part 2
badge_priorities = []
skip = 0
for index,line in enumerate(data):
    if skip > 0:
        skip -= 1
        continue
    else:
        elf1 = set(line.strip())
        elf2 = set(data[index+1].strip())
        elf3 = set(data[index+2].strip())
        
        badge = list(set.intersection(elf1,elf2,elf3))[0]
        badge_priorities.append(priority_lookup[badge])
        
        skip = 2
        
print(f'Part 2: Sum of priorities of the badges = {sum(badge_priorities)}')