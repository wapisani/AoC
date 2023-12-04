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
                # print(digits)
                # print(f"x: {i}, y: {j}")
                digits = ''
                
                
    
            else:
                continue
            
            
print(f"The sum of all of the part numbers in the engine schematic is {sum(numbers_with_symbols_adj)}")            
        



# Part 2 Solution

adj_to_indices = {'top_left': (-1,-1), 'top': (-1,0), 'top_right': (-1,1),
                  'left': (0,-1), 'right': (0,1),
                  'bottom_left': (1,-1), 'bottom': (1,0), 'bottom_right': (1,1)}


gear_ratios = []
skip_count = 0
found_values = []
gear_indices = [] # List of tuples (i,j), list of gear locations
for i in range(xlen):
    for j in range(ylen):
        cell = grid[i][j]
        if cell == '*':
            gear_indices.append((i,j))

for gear_ij in gear_indices:
    gi, gj = gear_ij
    adj = searchAdjacentGrid(grid, gi, gj)
    found_digits = []
    for key in adj:
        value = adj[key]
        if value.isdigit():
            nij = adj_to_indices[key]
            ni = gi + nij[0]
            nj = gj + nij[1]
            digits = [grid[ni][nj]]
            
            # Search for rest of digit
            left = -1
            while True:
                if nj + left < 0:
                    break
                else:
                    cell = grid[ni][nj + left]
                    if cell.isdigit():
                        digits.insert(0,cell)
                        left -= 1
                    else:
                        break
            
            right = 1
            while True:
                if nj + right > len(grid[ni][:]) - 1:
                    break
                else:
                    cell = grid[ni][nj + right]
                    if cell.isdigit():
                        digits.append(cell)
                        right += 1
                    else:
                        break
            
            digits_str = ''.join(digits)
            if digits_str in found_digits:
                continue
            else:
                found_digits.append(digits_str)
    if len(found_digits) == 2:
        fv = '-'.join(found_digits)
        found_values.append(fv)
        gear_ratios.append(int(found_digits[0])*int(found_digits[1]))
        
print(f"Sum of the gear ratios is {sum(gear_ratios)}")
