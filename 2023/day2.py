# -*- coding: utf-8 -*-
"""
@author: Will Pisani

"""

import os

directory = r'F:\Documents\Programming\AoC\2023'
os.chdir(directory)

with open('input_day2.txt','r') as handle:
    data = handle.readlines()

# Part 1 Solution

# data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""".split('\n')


games = [] # List of dicts
# Keys: ID: int, n_sets: int, 
# red: list of ints, blue: list of ints, 
# green: list of ints

possible_games = [] # List of ints
bag_red = 12
bag_green = 13
bag_blue = 14

for line in data:
    game_possible_flag = True
    g = {}
    game_id = int(line.split(':')[0].split('Game ')[-1])
    g['ID'] = game_id
    g_sets = line.strip().split(':')[1].split(';')
    n_sets = len(g_sets)
    g['n_sets'] = n_sets
    g['red'] = []
    g['blue'] = []
    g['green'] = []
    
    for n in range(n_sets):
        blue, red, green = 0, 0, 0 # In case a color doesn't show in a set
        g_set = g_sets[n].lstrip().split(',')
        for item in g_set:
            num_cubes, color = item.lstrip().split(' ')
            num_cubes = int(num_cubes)
            if color == 'green':
                green = num_cubes
                if green > bag_green:
                    game_possible_flag = False
                    
            elif color == 'blue':
                blue = num_cubes
                if blue > bag_blue:
                    game_possible_flag = False
                    
            elif color == 'red':
                red = num_cubes
                if red > bag_red:
                    game_possible_flag = False
                
        g['red'].append(red)
        g['green'].append(green)
        g['blue'].append(blue)
        
        
    games.append(g)
    
    if game_possible_flag:
        possible_games.append(game_id)
        
print(f"The sum of the IDs of the possible games are: {sum(possible_games)}.")   

    


# Part 2 Solution

powers = []
for g in games:
    min_red = max(g['red'])
    min_blue = max(g['blue'])
    min_green = max(g['green'])
    power = min_red * min_blue * min_green
    powers.append(power)

print(f"The sum of the power of the sets is {sum(powers)}")
