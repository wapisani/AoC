# -*- coding: utf-8 -*-
"""
@author: wapisani
"""

import os
import numpy as np
from collections import Counter

directory = r'F:\Documents\Programming\AoC\2021'
os.chdir(directory)

with open('input_day3.txt','r') as handle:
    data = handle.readlines()

# Test data
# data = ['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010']

data = [line.strip() for line in data]
# Store bits in array so that they're easily accessed later
rows, cols = len(data), len(data[0])
storage_array = np.zeros((rows,cols))
for i,line in enumerate(data):
    for j,bit in enumerate(line):
        bit = int(bit)
        storage_array[i,j] = bit

### Part 1 ###
gamma = ''
epsilon = ''
common_bits = ''
for col in range(cols):
    count = Counter(storage_array[:,col])
    zero_count = count[0.0]
    one_count = count[1.0]
    
    if zero_count > one_count:
        gamma += '0'
        epsilon += '1'
        common_bits += '0'
    elif one_count > zero_count:
        gamma += '1'
        epsilon += '0'
        common_bits += '1'
    else:
        common_bits += '='
    
        
print(f'Power consumption is {int(gamma,2)*int(epsilon,2)}')
    
### Part 2 ###
# Check for oxygen generator rating
def CheckCommonality(lines,col):
    """
    This function will check for the commonality of 1's vs 0's for a list
    of lines (given as lines) for a specific column position (given as col)
    and return which is greater or if they're equal.

    Parameters
    ----------
    lines : list
        list of strings of binary numbers.
    col : int
        column position.

    Returns
    -------
    '1', '0', or '='.

    """
    rows, cols = len(lines), len(lines[0])
    storage_array = np.zeros((rows,cols))
    for i,line in enumerate(lines):
        for j,bit in enumerate(line):
            bit = int(bit)
            storage_array[i,j] = bit
    
    count = Counter(storage_array[:,col])
    zero_count = count[0.0]
    one_count = count[1.0]
    
    if zero_count > one_count:
        return '0'
        
    elif one_count > zero_count:
        return '1'
        
    else:
        return '='
    
data_o2 = data[:]
for col in range(cols):
    if col > 0:
        more_common = CheckCommonality(data_o2, col)
    else:
        more_common = common_bits[col]
    if len(data_o2) == 1:
        break
    
    for line in data:
        if line not in data_o2:
            continue
        bit = line[col]
        if more_common == '=':
            if bit != '1':
                data_o2.remove(line)
                continue
        else:
            if bit != more_common:
                data_o2.remove(line)
                continue
o2 = int(data_o2[0],2)

data_co2 = data[:]
for col in range(cols):
    if col > 0:
        more_common = CheckCommonality(data_co2, col)
    else:
        more_common = common_bits[col]
    if len(data_co2) == 1:
        break
    
    for line in data:
        if line not in data_co2:
            continue
        bit = line[col]
        if more_common == '=':
            if bit != '0':
                data_co2.remove(line)
                continue
        else:
            if bit == more_common:
                data_co2.remove(line)
                continue
co2 = int(data_co2[0],2)

print(f'Life support rating is {co2*o2}')
