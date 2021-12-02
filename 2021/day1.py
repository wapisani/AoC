# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 18:37:36 2021

@author: wapisani
"""

import os
import numpy as np

directory = r'F:\Documents\Programming\AoC\2021'
os.chdir(directory)

with open('input_day1.txt','r') as handle:
    data = handle.readlines()
    
data_int = [int(x) for x in data]
deltas = []
for index,value in enumerate(data_int[1:]):
    delta = value - data_int[index]
    deltas.append(delta)

# Now count the number of positive values
pos_count = 0
for value in deltas:
    if value > 0:
        pos_count += 1

print(f'Star 1, number of increasing measurements = {pos_count}')

############ Star 2 #################
# Moving average function I found elsewhere years ago
def moving_sum(a, n):
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:]

window1 = moving_sum(data_int,3)
window2 = moving_sum(data_int[1:],3)
count_star2 = 0
for index,value in enumerate(window1):
    try:
        if window2[index] > value:
            count_star2 += 1
    except:
        break
  
print(f'Star 2, number of increasing measurements = {count_star2}')
      