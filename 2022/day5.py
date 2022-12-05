# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 12:47:43 2022

@author: wapisani
"""

import os, re
from collections import deque
from copy import deepcopy

directory = r'F:\Documents\Programming\AoC\2022'
os.chdir(directory)

with open('input_day5.txt','r') as handle:
    data = handle.readlines()
    
# Part 1
stacks = {i: deque() for i in range(1,10)}
# For 9 stacks the letters occur on certain numbers from the start
# So I used that to create a lookup for which stack to add the letter
lookup = {1:1,5:2,9:3,13:4,17:5,21:6,25:7,29:8,33:9}
for line in data[0:8]: # from manual inspection of the input file
    line = line.strip('\n')
    for i,c in enumerate(line):
        if c.isalpha():
            stacks[lookup[i]].append(c)
            
stacks_part2 = deepcopy(stacks)
# Read through and execute the move instructions
# Starts on line 10 of the input deck
for line in data[10:]:
    line = line.strip().split(' ')
    num_to_move = int(line[1])
    from_stack = int(line[3])
    to_stack = int(line[-1])
    for n in range(1,num_to_move+1):
        stacks[to_stack].appendleft(stacks[from_stack].popleft())


top_crates = []
for stack_id in stacks:
    stack = stacks[stack_id]
    top_crates.append(stack[0])
    
print(f"The crates on top of each stack are {''.join(top_crates)}")

# Part 2

for i,line in enumerate(data[10:]):
    line = line.strip().split(' ')
    num_to_move = int(line[1])
    from_stack = int(line[3])
    to_stack = int(line[-1])
    if num_to_move > 1:
        temp_stack = []
        for n in range(num_to_move):
            temp_stack.append(stacks_part2[from_stack].popleft())
            
        for crate in temp_stack[::-1]:
            stacks_part2[to_stack].appendleft(crate)
    else:
        stacks_part2[to_stack].appendleft(stacks_part2[from_stack].popleft())
    
top_crates2 = []
for stack_id in stacks_part2:
    stack = stacks_part2[stack_id]
    top_crates2.append(stack[0])
    
print(f"The crates on top of each stack are {''.join(top_crates2)}")    
