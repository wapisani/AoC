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

# data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".split('\n')

# We start with 1 copy of each card
cards_won = [1 for line in data]

# Begin iterating through the cards
for i,line in enumerate(data):
    
    numbers = line.split(':')[1]
    winning_numbers, numbers_I_have = numbers.split('|')
    winning_numbers = winning_numbers.strip().split()
    numbers_I_have = numbers_I_have.strip().split()
    matches = 0
    for n in numbers_I_have:
        if n in winning_numbers:
            matches += 1
    # For each match, the current card i wins a copy of card i + N_match.
    # So we need to update the card counts for each copy.
    # However, we don't just update them by 1 because your x copies of card 2
    # will win the next two cards. So we have to increase the next two card
    # counts by x copies of card 2.
    for m in range(i+1,i+1+matches):
        cards_won[m] += cards_won[i]

print(f"We end up with {sum(cards_won)} total scratchcards")

        
        
    

