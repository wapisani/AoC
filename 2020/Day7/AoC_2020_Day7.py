# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 16:04:57 2020

@author: wapisani
"""

import os,re
from collections import defaultdict
import networkx as nx

os.chdir(r"F:\Documents\Programming\AoC\2020\Day7")

with open("input_Day7.txt",'r') as aoc_input:
    rule_list = aoc_input.read().split('\n')
    
rule_list = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.""".split('\n')
# The solution pretty much comes from this link
# https://dev.to/cnille/advent-of-code-2020-day-07-3da8
rules = defaultdict(dict)

for rule in rule_list:
    bag_rule = re.match(r'(.*) bags contain',rule).groups()[0]
    for count,r in re.findall(r'(\d+) (\w+ \w+) bag',rule):
        rules[bag_rule][r] = {'weight': int(count)}
    
# Add rules to directed graph
G = nx.DiGraph(rules)

# Use networkx to find the number of bag colors that can eventually contain 
# at least one shiny gold bag.
# The graph is currently oriented such that the bags contain other bags.
# I want to find the number of bags that can contain the shiny gold so the
# graph needs to be reversed.
bag_colors = nx.dfs_predecessors(G.reverse(),'shiny gold')

print(f"In part 1, the number of bag colors that can eventually contain at\
      least one shiny gold bag is {len(bag_colors)}")

