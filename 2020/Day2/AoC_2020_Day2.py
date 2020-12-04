#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 20:52:05 2020

@author: wapisani
"""

def parsePasswordPolicy(string):
    split_pass = string.split(' ')
    min_policy = int(split_pass[0].split('-')[0])
    max_policy = int(split_pass[0].split('-')[1])
    policy = split_pass[1][0] 
    password = split_pass[2]
    return min_policy, max_policy, policy, password

def isValidPassword(min_policy,max_policy,policy,password):
    matches = re.findall(policy,password)
    if len(matches) >= min_policy and len(matches) <= max_policy:
        return True
    else:
        return False
    
    
# Import necessary libraries
import os,re

os.chdir(r"/Users/wapisani/Documents/Programming/AoC/2020/Day2")

with open("input_Day2.txt","r") as aoc_input:
    passwords = [line.rstrip() for line in aoc_input]
    
valid_passwords_part1 = []


for element in passwords:
    min_policy, max_policy, policy, password = parsePasswordPolicy(element)
    
    validity = isValidPassword(min_policy,max_policy,policy,password)
    if validity == True:
        valid_passwords_part1.append(password)
        

print(f"In part 1, there are {len(valid_passwords_part1)} valid passwords.\n")

valid_passwords_part2 = []
for element in passwords:
    min_policy, max_policy, policy, password = parsePasswordPolicy(element)
    pos1 = password[min_policy-1]
    pos2 = password[max_policy-1]
    
    position_counter = 0
    if pos1 == policy:
        position_counter += 1
    
    if pos2 == policy:
        position_counter += 1
        
    if position_counter == 1:
        valid_passwords_part2.append(password)
        
print(f"In part 2, there are {len(valid_passwords_part2)} valid passwords.")
    
    
    
    
    
    
    
    

