# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 14:24:09 2020

@author: wapisani
"""
import os,math

os.chdir(r"F:\Documents\Programming\AoC\2020\Day5")

with open("input_Day5.txt",'r') as aoc_input:
    boarding_passes = aoc_input.read().split('\n')
    
seat_ids = []
for boarding_pass in boarding_passes:
    
    # boarding_pass = 'FBFBBFFRLR'
    row_letters = boarding_pass[0:7]
    column_letters = boarding_pass[7:]
    row_binary = ''
    for letter in row_letters:
        if letter == 'F':
            row_binary += '0'
        elif letter == 'B':
            row_binary += '1'
            
    row_decimal = int(row_binary,2)
    col_binary = ''
    for letter in column_letters:
        if letter == 'L':
            col_binary += '0'
        elif letter == 'R':
            col_binary += '1'
    col_decimal = int(col_binary,2)

    seat_id = row_decimal*8 + col_decimal
    seat_ids.append(seat_id)

print(f"In part 1, the highest seat ID on a boarding pass is {max(seat_ids)}")

seats = range(min(seat_ids),max(seat_ids))
for seat in seats:
    if seat not in seat_ids:
        print(f"Your seat is {seat}")
        break


