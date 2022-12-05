# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 16:34:24 2022

@author: wapisani
"""
import os

directory = r'F:\Documents\Programming\AoC\2022'
os.chdir(directory)

with open('input_day4.txt','r') as handle:
    data = handle.readlines()
    
# Part 1    
assignment1 = []
assignment2 = []
pairs = 0
for line in data:
    first_range, second_range = line.strip().split(',')
    range1_start, range1_stop = map(int,first_range.split('-'))
    range2_start, range2_stop = map(int,second_range.split('-'))
    assign1 = list(range(range1_start,range1_stop+1))
    assign2 = list(range(range2_start,range2_stop+1))
    assignment1.append(assign1)
    assignment2.append(assign2)
    
    one_in_two_flag = True
    for i in assign1:
        if i not in assign2:
            one_in_two_flag = False
            break
    
    two_in_one_flag = True
    for j in assign2:
        if j not in assign1:
            two_in_one_flag = False
            break
  
    if one_in_two_flag == True or two_in_one_flag == True:
        pairs += 1
        
print(f"The number of pairs where one range fully contains the other is {pairs}.")
    
    
# Part 2
pairs_that_overlap = 0
for i,assign1 in enumerate(assignment1):
    assign2 = assignment2[i]
    
    one_overlap_flag = False
    for j in assign1:
        if j in assign2:
            one_overlap_flag = True
            break
        
    two_overlap_flag = False
    for k in assign2:
        if k in assign1:
            two_overlap_flag = True
            break
    if one_overlap_flag == True or two_overlap_flag == True:
        pairs_that_overlap += 1

print(f"The number of assignment pairs where the ranges overlap is {pairs_that_overlap}")
    
    
    
    
    