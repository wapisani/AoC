# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 12:08:04 2022

@author: wapisani
"""

import os

directory = r'F:\Documents\Programming\AoC\2022'
os.chdir(directory)

with open('input_day2.txt','r') as handle:
    data = handle.readlines()
    
# Part 1
convert_lookup = {'X': 'A', 'Y': 'B', 'Z': 'C'}
value_lookup = {'A': 1, 'B': 2, 'C': 3}
matchup_values = {'A-B': 6, 'B-A': 0, 'A-C': 0,
                  'C-A': 6, 'C-B': 0, 'B-C': 6}

total_score = 0
for line in data:
    columns = line.strip().split(' ')
    elf_play = columns[0]
    my_play = convert_lookup[columns[1]]
    
    shape_score = value_lookup[my_play]
    if elf_play == my_play:
        outcome = 3
    else:
        outcome = matchup_values[f'{elf_play}-{my_play}']
    score = outcome + shape_score
    total_score += score

print(f'Part 1: My total score is {total_score}.')
    

# Part 2
# X = Lose, Y = Draw, Z = Win
total_score = 0
shape_lookup = {'X': {'A': 'C', 'B': 'A', 'C': 'B'},
               'Y': {'A': 'A', 'B': 'B', 'C': 'C'},
               'Z': {'A': 'B', 'B': 'C', 'C': 'A'}}
outcome_lookup = {'X': 0, 'Y': 3, 'Z': 6}
for line in data:
    columns = line.strip().split(' ')
    elf_play = columns[0]
    win_cond = columns[1]
    outcome_score = outcome_lookup[win_cond]
    shape = shape_lookup[win_cond][elf_play]
    shape_score = value_lookup[shape]
    score = outcome_score + shape_score
    total_score += score

print(f'Part 2: My total score is {total_score}.')
        
    