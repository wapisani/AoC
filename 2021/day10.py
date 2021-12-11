# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 17:52:06 2021

@author: wapisani
"""

import os

directory = r'F:\Documents\Programming\AoC\2021'
os.chdir(directory)

# with open('input_day10.txt','r') as handle:
#     data = [line.strip() for line in handle.readlines()]
   

with open('sample_day10.txt','r') as handle:
    data = [line.strip() for line in handle.readlines()]
    
lookup_table = {')': 3,
                ']': 57,
                '}': 1197,
                '>': 25137}

illegal_chars = []
left = '[({<'
right = '])}>'
for line in data[:]:
    stack = []
    for char in line:
        if char in left:
            stack.append(char)
        elif char in right:
            top = stack[-1]
            i = left.index(top)
            if char == right[i]:
                stack.pop()
            else:
                print(f'Found {char} expected {right[i]}')
                illegal_chars.append(char)
                data.pop(data.index(line))
                break


# Calculate points
points = 0
for char in illegal_chars:
    points += lookup_table[char]

print(f'The total syntax error score is {points}')
    
### Part 2 ###

# Try using the stack method for this part
# The exact sequence matters
left_count = {'[': 0, '(': 0, '{': 0, '<': 0}
right_count = {']': 0, ')': 0, '}': 0, '>': 0}
sequences = []
for line in data:
    left_count = {'[': 0, '(': 0, '{': 0, '<': 0}
    right_count = {']': 0, ')': 0, '}': 0, '>': 0}
    for char in line:
        if char in left:
            left_count[char] += 1
        elif char in right:
            right_count[char] += 1
            
    count_diff = []
    count_diff.append(left_count['[']-right_count[']'])
    count_diff.append(left_count['(']-right_count[')'])   
    count_diff.append(left_count['{']-right_count['}'])   
    count_diff.append(left_count['<']-right_count['>'])  
    seq = ''
    seq += ']'*count_diff[0]
    seq += ')'*count_diff[1]
    seq += '}'*count_diff[2]
    seq += '>'*count_diff[3]
    sequences.append(seq)

        