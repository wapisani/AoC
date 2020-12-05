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

passport_dict_list = []
for passport in passports:
    passport = re.sub("\n"," ",passport).rstrip()
    passport_dict = {}
    for field in passport.split(" "):
        field_split = field.split(":")
        passport_dict[field_split[0]] = field_split[1]
    passport_dict_list.append(passport_dict)

for passport in passport_dict_list[:]:
    if "byr" not in passport:
        continue
    elif "iyr" not in passport:
        continue
    elif "eyr" not in passport:
        continue
    elif "hgt" not in passport:
        continue
    elif "hcl" not in passport:
        continue
    elif "ecl" not in passport:
        continue
    elif "pid" not in passport:
        continue
    else:
        # Birth year, four digits; at least 1920 and at most 2002.
        byr = passport['byr']
        if len(byr) != 4:
            continue
        else:
            if int(byr) < 1920 or int(byr) > 2002:
                continue
        
        # Issue year, four digits; at least 2010 and at most 2020.
        iyr = passport['iyr']
        if len(iyr) != 4:
            continue
        else:
            if int(iyr) < 2010 or int(iyr) > 2020:
                continue
            
        # Expiration year, four digits; at least 2020 and at most 2030.
        eyr = passport['eyr']
        if int(eyr) < 2020 or int(eyr) > 2030:
            continue
        
        # Height
        hgt = passport['hgt']
        if "cm" not in hgt and "in" not in hgt:
            continue
        else:
            if "cm" in hgt:
                hgt_num = int(hgt.split("cm")[0])
                if hgt_num < 150 or hgt_num > 193:
                    continue
            elif "in" in hgt:
                hgt_num = int(hgt.split("in")[0])
                if hgt_num < 59 or hgt_num > 76:
                    continue
                
        # Hair color
        hcl = passport['hcl']
        hcl_check = "#0123456789abcdef"
        if '#' not in hcl:
            continue
        hcl_flag = False
        for character in hcl:
            if character not in hcl_check:
                hcl_flag = True
                break
        if hcl_flag:
            continue
        
        # Eye color
        ecl = passport['ecl']
        if len(ecl) != 3:
            continue
        ecl_check = "ambblubrngrygrnhzloth"
        if ecl not in ecl_check:
            continue
        
        # Passport ID
        pid = passport['pid']
        if len(pid) != 9:
            continue
        pid_check = "0123456789"
        pid_flag = False
        for character in pid:
            if character not in pid_check:
                pid_flag = True
                break
        if pid_flag:
            continue
        
        valid_passports_pt2.append(passport)

print(f"In part 2, there are {len(valid_passports_pt2)} valid passports.")
            
        
            
            
            
            
            
            
            
            
            
            
            
            