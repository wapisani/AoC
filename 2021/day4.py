# -*- coding: utf-8 -*-
"""
@author: wapisani
"""

import os
import numpy as np


directory = r'F:\Documents\Programming\AoC\2021'
os.chdir(directory)

with open('input_day4.txt','r') as handle:
    data = handle.readlines()

# Test data

data = [line.strip() for line in data]
while "" in data: # Remove empty strings in-between bingo boards
    data.remove("")
    
bingo_order = data[0].split(',')
numbers = [int(value) for value in bingo_order]
boards = []
start = 1
stop = start + 5
count = 0
for line in data[1:]:
    if count > len(data[2:])/5: # There will only be len(data[2:])/5 boards
        break
    # stop = start + 5
    matrix_lines = data[start:stop]
    matrix = []
    for mline in matrix_lines:
        mline = mline.split(' ')
        row = []
        for col in mline:
            if col == '':
                continue
            row.append(int(col))
        matrix.append(row)
    boards.append(matrix)
    count += 1
    start += 5
    stop += 5


# Convert to numpy arrays
boards_np = np.zeros((len(boards),5,5)) # First number is actually z-dimension
boards_bingo = np.zeros((len(boards),5,5))
for z,board in enumerate(boards):
    boards_np[z,:,:] = np.asarray(board)

# Start reading off the numbers
break_flag = False
for value in numbers:
    
    for index,board in enumerate(boards_np):
        if value in board:
            r,c = np.where(board==value)
            boards_bingo[index,r,c] = 1 # 1 is a mark
            
        # Check for bingo's
        # In this part bingo's only count if they are rows or columns.
        # Since I'm using 1's for marks, there will be a bingo if there is a sum
        # of 5 for any given row or column
        # Check rows
        board_marks = boards_bingo[index,:,:]
        for row in range(5):
            sum_value = np.sum(board_marks[row,:])
            if sum_value > 4: # Winner!!
                print(f'board {board} is a winner at row {row}')
                print(f'{board_marks}')
                print('Now summing all unmarked numbers...')
                unmark_row, unmark_col = np.where(board_marks==0)
                unmark_sum = 0
                for index,unmark in enumerate(unmark_row):
                    x = unmark
                    y = unmark_col[index]
                    unmark_sum += board[x,y]
                print(f'The sum of all unmarked numbers is {unmark_sum}')
                print(f'The number that was just called is {value}.')
                print(f'Your final score is {unmark_sum*value}.')
                break_flag = True
                break
                
        
        for col in range(5):
            sum_value = np.sum(board_marks[:,col])
            if sum_value > 4: # Winner!!
                print(f'board {board} is a winner at column {col}')
                print(f'{board_marks}')
                print('Now summing all unmarked numbers...')
                unmark_row, unmark_col = np.where(board_marks==0)
                unmark_sum = 0
                for index,unmark in enumerate(unmark_row):
                    x = unmark
                    y = unmark_col[index]
                    unmark_sum += board[x,y]
                print(f'The sum of all unmarked numbers is {unmark_sum}')
                print(f'The number that was just called is {value}.')
                print(f'Your final score is {unmark_sum*value}.')
                break_flag = True
                break
        
        if break_flag:
            break
    if break_flag:
        break
            
     
### Part 2 ###
# To find the last board that will win, create an array of zeros that matches
# the number of boards. Change each zero to a 1 when that board wins.
# When the sum of the array matches the number of boards, stop and print that 
# board. Or just print every board win, but stop the code. The last one to print
# will be the last one to win.        
