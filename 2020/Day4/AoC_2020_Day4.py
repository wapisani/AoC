#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 23:16:40 2020

@author: wapisani
"""

import os,re

os.chdir(r"/Users/wapisani/Documents/Programming/AoC/2020/Day4")

with open("input_Day4.txt",'r') as aoc_input:
    passports = aoc_input.read().split('\n\n')
    
valid_passports_pt1 = []
for passport in passports:
    
    if "byr:" not in passport:
        continue
    elif "iyr:" not in passport:
        continue
    elif "eyr:" not in passport:
        continue
    elif "hgt:" not in passport:
        continue
    elif "hcl:" not in passport:
        continue
    elif "ecl:" not in passport:
        continue
    elif "pid:" not in passport:
        continue
    else:
        valid_passports_pt1.append(passport)
    
print(f"In part 1, there are {len(valid_passports_pt1)} valid passports.\n")

valid_passports_pt2 = []
# Too low at 109, too high at 124, not 120
# example = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
# hcl:#623a2f

# eyr:2029 ecl:blu cid:129 byr:1989
# iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

# hcl:#888785
# hgt:164cm byr:2001 iyr:2015 cid:88
# pid:545766238 ecl:hzl
# eyr:2022

# iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""
# passports = example.split('\n\n')


for passport in passports:
    # Initial check
    if "byr:" not in passport:
        continue
    elif "iyr:" not in passport:
        continue
    elif "eyr:" not in passport:
        continue
    elif "hgt:" not in passport:
        continue
    elif "hcl:" not in passport:
        continue
    elif "ecl:" not in passport:
        continue
    elif "pid:" not in passport:
        continue
    else:
        # Now check each field
        # Birth year, four digits; at least 1920 and at most 2002.
        birth_year = re.findall("byr:([0-9]{4})",passport)[0]
        if int(birth_year) < 1920 or int(birth_year) > 2002:
            continue
        # Issue year, four digits; at least 2010 and at most 2020.
        issue_year = re.findall("iyr:([0-9]{4})",passport)[0]
        if int(issue_year) < 2010 or int(issue_year) > 2020:
            continue
        # Expiration year, four digits; at least 2020 and at most 2030.
        exp_year = re.findall("eyr:([0-9]{4})",passport)[0]
        if int(exp_year) < 2020 or int(exp_year) > 2030:
            continue
        # Height
        
        height = re.findall("hgt:([0-9]+cm|[0-9]+in)",passport)
        if len(height) == 0: # Could not find cm or in if the list is empty
            continue
        else:
            height_num = re.findall("[0-9]+",height[0])[0]
            height_num = int(height_num)
            if "cm" in height:
                if height_num < 150 or height_num > 193:
                    continue
            elif "in" in height:
                if height_num < 59 or height_num > 76:
                    continue
        # Hair color
        hair_color = re.findall("hcl:#(\w{6})",passport)
        if len(hair_color) == 0: # If no match
            continue
        # Eye color
        eye_color = re.findall("ecl:(amb{1}|blu{1}|brn{1}|gry{1}|grn{1}|hzl{1}|oth{1})",passport)
        if len(eye_color) == 0: # If no match
            continue
        # Passport ID
        passport_id = re.findall("pid:([0-9]{9})",passport)      
        if len(passport_id) == 0: # If no match
            continue
        
        valid_passports_pt2.append(passport)

print(f"In part 2, there are {len(valid_passports_pt2)} valid passports.")
            
        
            
            
            
            
            
            
            
            
            
            
            
            