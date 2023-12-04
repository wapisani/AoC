# -*- coding: utf-8 -*-
"""
@author: Will Pisani

"""

import os

directory = r'F:\Documents\Programming\AoC\2023'
os.chdir(directory)

with open('input_day3.txt','r') as handle:
    data = handle.readlines()

# Part 1 Solution

# data = """467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..""".split('\n')

def searchAdjacentGrid(grid,i,j):
    """
    This function will search the adjacent cells of the specified cell in a 
    grid and return what they contain.

    Parameters
    ----------
    grid : A list of lists
        A standard Python 2D array. The cells can be anything 
        (string, int, float, etc.).
    i : int
        x-dimension cell index.
    j : int
        y-dimension cell index.

    Returns
    -------
    adj_grid : dict
        A dictionary with the contents of the adjacent cells.

    """
    adj_grid = {'top_left': 'N/A', 'top': 'N/A', 'top_right': 'N/A',
                'left': 'N/A', 'right': 'N/A',
                'bottom_left': 'N/A', 'bottom': 'N/A', 'bottom_right': 'N/A'}
    
    if i == 0 and j == 0: # first row, first column
        adj_grid['right'] = grid[i][j+1]
        adj_grid['bottom'] = grid[i+1][j]
        adj_grid['bottom_right'] = grid[i+1][j+1]
        
    elif i == 0 and j == len(grid[:][0]) -1: # first row, last col
        adj_grid['left'] = grid[i][j-1]
        adj_grid['bottom_left'] = grid[i+1][j-1]
        adj_grid['bottom'] = grid[i+1][j]
        
    elif i == len(grid) - 1 and j == 0: # last row, first column
        adj_grid['top'] = grid[i-1][j]
        adj_grid['top_right'] = grid[i-1][j+1]
        adj_grid['right'] = grid[i][j+1]
        
    elif i == len(grid) - 1 and j == len(grid[:][0]) - 1: # last row, last column
        adj_grid['top_left'] = grid[i-1][j-1]
        adj_grid['top'] = grid[i-1][j]
        adj_grid['left'] = grid[i][j-1]
        
    elif i == 0 and 0 < j < len(grid[:][0]) - 1: # first row
        adj_grid['left'] = grid[i][j-1]
        adj_grid['right'] = grid[i][j+1]
        adj_grid['bottom_left'] = grid[i+1][j-1]
        adj_grid['bottom'] = grid[i+1][j]
        adj_grid['bottom_right'] = grid[i+1][j+1]
        
    elif i == len(grid) - 1 and 0 < j < len(grid[:][0]) - 1: # last row
        adj_grid['top_left'] = grid[i-1][j-1]
        adj_grid['top'] = grid[i-1][j]
        adj_grid['top_right'] = grid[i-1][j+1]
        adj_grid['left'] = grid[i][j-1]
        adj_grid['right'] = grid[i][j+1]
        
    elif 0 < i < len(grid) - 1 and j == 0: # first column
        adj_grid['top'] = grid[i-1][j]
        adj_grid['top_right'] = grid[i-1][j+1]
        adj_grid['right'] = grid[i][j+1]
        adj_grid['bottom'] = grid[i+1][j]
        adj_grid['bottom_right'] = grid[i+1][j+1]
        
    elif 0 < i < len(grid) - 1 and j == len(grid[:][0]) - 1: # last column
        adj_grid['top_left'] = grid[i-1][j-1]
        adj_grid['top'] = grid[i-1][j]
        adj_grid['left'] = grid[i][j-1]
        adj_grid['bottom_left'] = grid[i+1][j-1]
        adj_grid['bottom'] = grid[i+1][j]
    else:
        adj_grid['top_left'] = grid[i-1][j-1]
        adj_grid['top'] = grid[i-1][j]
        adj_grid['top_right'] = grid[i-1][j+1]
        adj_grid['left'] = grid[i][j-1]
        adj_grid['right'] = grid[i][j+1]
        adj_grid['bottom_left'] = grid[i+1][j-1]
        adj_grid['bottom'] = grid[i+1][j]
        adj_grid['bottom_right'] = grid[i+1][j+1]
    
    return adj_grid
        
        
        

grid = []
for line in data:
    line = line.strip()
    grid.append([c for c in line])
    


xlen = len(grid)
ylen = len(grid[0][:])

# Search grid for symbols
symbols = []
for i in range(xlen):
    for j in range(ylen):
        cell = grid[i][j]
        if cell != '.' and cell.isdigit() == False:
            if cell not in symbols:
                symbols.append(cell)
   
numbers_with_symbols_adj = []
skip_count = 0
for i in range(xlen):
    x = grid[i]
    digits = ''
    for j in range(ylen):
        if skip_count > 0:
            skip_count -= 1
            continue
        y = grid[i][j]
        if y == '.' or y in symbols:
            digits = ''
            continue
        elif y.isdigit():
            digits += y
            
            adj_grid = searchAdjacentGrid(grid, i, j)
            
            symbol_flag = False
            for s in symbols:
                if s in adj_grid.values():
                    symbol_flag = True
                    break
            
            if symbol_flag:
                # search to the right for more digits
                skip_count = 0
                for k in range(j+1,ylen):
                    cell = grid[i][k]
                    if cell.isdigit():
                        digits += cell
                        skip_count += 1
                    else:
                        break
                    
                numbers_with_symbols_adj.append(int(digits))
                print(digits)
                print(f"x: {i}, y: {j}")
                digits = ''
                
                
    
            else:
                continue
            
            
print(f"The sum of all of the part numbers in the engine schematic is {sum(numbers_with_symbols_adj)}")            
        



# Part 2 Solution

adj_to_indices = {'top_left': (-1,-1), 'top': (-1,0), 'top_right': (-1,1),
                  'left': (0,-1), 'right': (0,1),
                  'bottom_left': (1,-1), 'bottom': (1,0), 'bottom_right': (1,1)}

import re

gear_ratios = []
skip_count = 0
for i in range(xlen):
    x = grid[i]
    digits = ''
    for j in range(ylen):
        first_num = 0
        if skip_count > 0:
            skip_count -= 1
            continue
        y = grid[i][j]
        if y == '.' or y in symbols:
            digits = ''
            continue
        elif y.isdigit():
            digits += y
            
            # Search adjacent cells for '*'
            adj_grid = searchAdjacentGrid(grid, i, j)
            
            # Get the indices of the '*' cell
            symbol_flag = False
            if '*' in adj_grid.values():
                # search to the right for more digits of the first num
                skip_count = 0
                for k in range(j+1,ylen):
                    cell = grid[i][k]
                    if cell.isdigit():
                        digits += cell
                        skip_count += 1
                    else:
                        break
                    
                for key in adj_grid:
                    value = adj_grid[key]
                    if value == '*':
                        indices = adj_to_indices[key]
                        break
                    
                first_num = int(digits) 
                # Use those indices to search the surrounding cells for 
                # more digits
                gear_i = i + indices[0]
                gear_j = j + indices[1]
                
                gear_adj_grid = searchAdjacentGrid(grid, gear_i, gear_j)
                
                for key in gear_adj_grid:
                    value = gear_adj_grid[key]
                    if value.isdigit():
                        digits_two = ''
                        # Get indices of any numbers
                        num_indicies = adj_to_indices[key]
                        num_i = gear_i + num_indicies[0]
                        num_j = gear_j + num_indicies[1]
                        
                        # search to the left
                        cells = grid[num_i][num_j-2:num_j+2]
                        digits_two = ''.join(cells)
                        
                        digits_two = re.sub(r'\.','',digits_two)
                        digits_two = re.sub(r'\*','',digits_two)
                        digits_two = re.sub(r'\&','',digits_two)
                        digits_two = re.sub(r'\%','',digits_two)
                        digits_two = re.sub(r'\/','',digits_two)
                        digits_two = re.sub(r'\#','',digits_two)
                        
                        second_num = int(digits_two)
                gear_ratios.append(first_num*second_num)
                
print(f"Sum of the gear ratios is {sum(gear_ratios)}")
                            
# 154899900 is too high                      
                    
                    
            
            
            
