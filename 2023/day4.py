# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 17:54:54 2023

@author: Will Pisani
"""

import os

directory = r'F:\Documents\Programming\AoC\2023'
os.chdir(directory)

with open('input_day4.txt','r') as handle:
    data = handle.readlines()

# Part 1 Solution

# data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".split('\n')

card_points = []
for line in data:
    numbers = line.split(':')[1]
    winning_numbers, numbers_I_have = numbers.split('|')
    winning_numbers = winning_numbers.strip().split()
    numbers_I_have = numbers_I_have.strip().split()
    points = 0
    matches = 0
    for n in numbers_I_have:
        if n in winning_numbers:
            matches += 1
            if matches == 1:
                points = 1
            else:
                points *= 2
                
    card_points.append(points)
    
print(f"The large pile of colorful cards are worth {sum(card_points)} points total")
            
# Part 2 solution

data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".split('\n')

# cards = {}
# for line in data:
#     card_id = int(line.split(':')[0].split()[1])
#     numbers = line.split(':')[1]
#     winning_numbers, numbers_I_have = numbers.split('|')
#     winning_numbers = winning_numbers.strip().split()
#     numbers_I_have = numbers_I_have.strip().split()
#     cards[card_id] = {'win': winning_numbers, 'have': numbers_I_have}

cards_won_dict = {} # Key of card id: value is the list of cards won
cards_won_list = []
for line in data:
    card_id = int(line.split(':')[0].split()[1])
    numbers = line.split(':')[1]
    winning_numbers, numbers_I_have = numbers.split('|')
    winning_numbers = winning_numbers.strip().split()
    numbers_I_have = numbers_I_have.strip().split()
    matches = 0
    for n in numbers_I_have:
        if n in winning_numbers:
            matches += 1
    if matches > 0:
        cards_won_dict[card_id] = [card for card in range(card_id+1,card_id+matches+1)]
    else:
        cards_won_dict[card_id] = []
    cards_won_list.append(matches)


        
        
    

