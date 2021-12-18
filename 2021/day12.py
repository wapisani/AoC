# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 14:43:04 2021

@author: wapisani
"""

import os
import numpy as np
import networkx as nx

directory = r'F:\Documents\Programming\AoC\2021'
# directory = r'/Users/wapisani/Documents/Programming/AoC/2021'
os.chdir(directory)

# with open('input_day12.txt','r') as handle:
#     data = [line.strip() for line in handle.readlines()]
   

with open('sample_day12.txt','r') as handle:
    data = [line.strip() for line in handle.readlines()]

edges = []
for line in data:
    edge = line.split('-')
    edges.append((edge[0],edge[1]))

G = nx.Graph()
for edge in edges:
    G.add_edge(*edge)
    
paths = nx.all_simple_paths(G, 'start', 'end')
