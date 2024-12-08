# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 12:20:09 2024

@author: wapisani
"""

import os, re
from operator import itemgetter

directory = r'F:\Documents\Programming\AoC\2024'
os.chdir(directory)

with open('input_day3.txt','r') as handle:
    data = handle.read()
    
# example data
# data = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""

all_matches = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)',data)

multiplications = []
for m in all_matches:
    first_int, sec_int = list(map(int,m.strip('mul(').strip(')').split(',')))
    multiplications.append(first_int*sec_int)
    
print('Part 1')
print(f'The sum of the multiplications is {sum(multiplications)}')

# example data
# data = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""
all_matches = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)',data)

# Get indices of don't() and do() instructions
do_not_indices = [x.start() for x in re.finditer(r"don't\(\)",data)]
do_indices = [x.start() for x in re.finditer(r"do\(\)",data)]

# Get indices of multiplication instructions
mul_indices = [x.start() for x in re.finditer(r'mul\([0-9]{1,3},[0-9]{1,3}\)',data)]

# Construct list of tuples
all_instructions = []
for i in do_not_indices:
    all_instructions.append(('disable',i))

for i in do_indices:
    all_instructions.append(('enable',i))

for index,i in enumerate(mul_indices):
    all_instructions.append(('multiply',i,all_matches[index]))

all_instructions = sorted(all_instructions,key=itemgetter(1)) # Sort by index

multiplications = []
disable_flag = False
for i in all_instructions:
    if i[0] == 'disable':
        disable_flag = True
        
    if i[0] == 'enable':
        disable_flag = False
        
    if i[0] == 'multiply' and not disable_flag:
        first_int, sec_int = list(map(int,i[2].strip('mul(').strip(')').split(',')))
        multiplications.append(first_int*sec_int)

print('\nPart 2')
print(f'The sum of all multiplications is {sum(multiplications)}')
        