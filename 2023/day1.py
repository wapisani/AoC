# -*- coding: utf-8 -*-
"""
@author: Will Pisani

"""

import os, re
from operator import itemgetter

directory = r'F:\Documents\Programming\AoC\2023'
os.chdir(directory)

with open('input_day1.txt','r') as handle:
    data = handle.readlines()

# Part 1 Solution

# data = """1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet""".split('\n')

values = []
for line in data:
    line = line.strip()
    digits = []
    for c in line:
        if c.isdigit():
            digits.append(c)
    
    values.append(int(digits[0] + digits[-1]))
        

print(f"The sum of all of the calibration values is {sum(values)}")  

# Part 2 Solution
# data = """two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen""".split('\n')

values = []
alpha_to_num = {'one': '1', 'two': '2', 'three': '3', 'four': '4',
                'five': '5', 'six': '6', 'seven': '7', 'eight': '8',
                'nine': '9', 'zero': '0'}

for line in data:
    line = line.strip()
        
    digits = [] # List of tuples (position,digit)
    
    # Iterate through line and pull out all digits first
    for index,c in enumerate(line):
        if c.isdigit():
            digits.append((index,c))
    
    # Iterate through alpha_to_num and check if keys are in line
    for key in alpha_to_num:
        if key in line:
            d = alpha_to_num[key]
            
            # Need to get position of all occurrences
            positions = [p.start() for p in re.finditer(key, line)]
            for p in positions:
                digits.append((p,d))
            
    # Sort digits based on the position, itemgetter is faster than lambda
    new_digits = sorted(digits,key=itemgetter(0))
    
    v = new_digits[0][1] + new_digits[-1][1]

    values.append(int(v))

print(f"The sum of all of the calibration values is {sum(values)}.")
