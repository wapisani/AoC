# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 17:52:06 2021

@author: wapisani
"""

import os

directory = r'F:\Documents\Programming\AoC\2021'
os.chdir(directory)

with open('input_day10.txt','r') as handle:
    data = [line.strip() for line in handle.readlines()]
   

# with open('sample_day10.txt','r') as handle:
#     data = [line.strip() for line in handle.readlines()]
    
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
sequences = []
for line in data[:]:
    stack = []
    seq = ''
    for char in line:
        if char in left:
            stack.append(char)
        elif char in right:
            top = stack[-1]
            i = left.index(top)
            if char == right[i]:
                stack.pop() # Pop all matches
            
    while stack: # Unbalanced brackets are the only thing left
        top = stack[-1]
        i = left.index(top)
        seq += right[i]
        stack.pop()
            
    sequences.append(seq)
            
p2_lookup = {')': 1, ']': 2, '}': 3, '>': 4}
scores = []
for seq in sequences:
    score = 0
    for char in seq:
        score *= 5
        score += p2_lookup[char]
    scores.append(score)

middle_score = sorted(scores)[len(scores)//2]
print(f'The middle score is {middle_score}')
        