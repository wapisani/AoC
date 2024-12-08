#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 23:30:28 2024

@author: wapisani
"""

import os, re
from operator import itemgetter
import numpy as np

directory = r'/home/wapisani/Documents/Programming/AoC/2024'
os.chdir(directory)

with open('input_day1.txt','r') as handle:
    data = handle.readlines()
    
# example data
# data = """3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3""".split('\n')

list1 = np.zeros((len(data)))
list2 = np.zeros((len(data)))

for index,line in enumerate(data):
    split_line = line.strip().split()
    list1[index], list2[index] = map(int,split_line)

list1.sort()
list2.sort()
distance = np.abs(list1 - list2)
print("Part 1")
print(f"The total distance is {np.sum(distance)}")

similarity_score = 0
for num1 in list1:
    similarity_score += np.count_nonzero(list2==num1)*num1

print("Part 2")
print(f"The similarity score is {similarity_score}")