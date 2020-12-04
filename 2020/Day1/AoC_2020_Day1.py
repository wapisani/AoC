#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 20:22:31 2020

@author: Will Pisani
"""

# Import necessary libraries
import os

# Change directory
os.chdir(r"/Users/wapisani/Documents/Programming/AoC/2020/Day1")

# Open input
with open("input_Day1.txt","r") as aoc_in:
    expense_report = [int(line) for line in aoc_in]
    
# Part 1
break_flag = False
for expense1 in expense_report:
    for expense2 in expense_report:
        expense_sum = expense1 + expense2
        if expense_sum == 2020:
            expense_product = expense1 * expense2
            print(f"The sum of {expense1} and {expense2} is {expense_sum}")
            print(f"The product of {expense1} and {expense2} is {expense_product}")
            break_flag = True
            break
    if break_flag:
        break
            
# Part 2
break_flag = False
for expense1 in expense_report:
    for expense2 in expense_report:
        for expense3 in expense_report:
            expense_sum = expense1 + expense2 + expense3
            if expense_sum == 2020:
                expense_product = expense1 * expense2 * expense3
                print(f"\nThe sum of {expense1}, {expense2}, and {expense3} is {expense_sum}")
                print(f"The product of {expense1}, {expense2}, and {expense3} is {expense_product}")
                break_flag = True
                break
        if break_flag:
            break
    if break_flag:
        break


