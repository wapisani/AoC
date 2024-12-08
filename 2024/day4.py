# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 13:59:48 2024

@author: wapisani
"""

import os
import regex as re
from operator import itemgetter

directory = r'F:\Documents\Programming\AoC\2024'
os.chdir(directory)

with open('input_day4.txt','r') as handle:
    data = handle.read()
    
# example data
data = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".split('\n')

data_grid = []
for line in data:
    data_grid.append([x for x in line])

# The following taken from https://stackoverflow.com/questions/6313308/get-all-the-diagonals-in-a-matrix-list-of-lists-in-python
# flakes' answer
nrows = len(data_grid)
ncols = len(data_grid[0])
cols = [[] for _ in range(ncols)]
rows = [[] for _ in range(nrows)]
fdiag = [[] for _ in range(nrows + ncols - 1)]
bdiag = [[] for _ in range(len(fdiag))]
min_bdiag = -nrows + 1

for x in range(ncols):
    for y in range(nrows):
        cols[x].append(data_grid[y][x])
        rows[y].append(data_grid[y][x])
        fdiag[x+y].append(data_grid[y][x])
        bdiag[x-y-min_bdiag].append(data_grid[y][x])

all_strings = []
for c in cols:
    all_strings.append(''.join(c))

for r in rows:
    all_strings.append(''.join(r))

for f in fdiag:
    if len(f) > 3:
        all_strings.append(''.join(f))

for b in bdiag:
    if len(b) > 3:
        all_strings.append(''.join(b))

# Now let's search for instances of XMAS and SAMX
all_strings_count = []
for s in all_strings:
    all_strings_count.append(len(re.findall(r'XMAS|SAMX',s,overlapped=True)))

print('Part 1')
print(f'There are {sum(all_strings_count)} instances of XMAS')
# for i,s in enumerate(all_strings):
#     print(f'{s} has {all_strings_count[i]} instances of XMAS or SAMX')