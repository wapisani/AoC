# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 15:15:06 2020

@author: wapisani
"""
import os,re

os.chdir(r"F:\Documents\Programming\AoC\2020\Day6")

with open("input_Day6.txt",'r') as aoc_input:
    answers = aoc_input.read().split('\n\n')
    
group_counts = []
group_count_sum = 0
for group_answers in answers:
    # Replace newlines with empty strings
    group_answers = re.sub('\n', '', group_answers)
    group_answers_set = set(group_answers)
    group_counts.append(len(group_answers_set))
    group_count_sum += len(group_answers_set)
    

print(f"In part 1, the sum of the counts is {group_count_sum}")

group_counts_pt2 = []
group_count_sum_pt2 = 0
for group_answers in answers:
    persons = group_answers.split('\n')
    if len(persons) == 1:
        group_counts_pt2.append(len(persons[0]))
        group_count_sum_pt2 += len(persons[0])
    else:
        # Create a dict to store occurences of questions
        # Each person can only answer each question once so questions
        # that have multiples answers across multiple people will have 
        # a value greater than 1
        question_dict = {}
        question_string = 'abcdefghijklmnopqrstuvwxyz'
        for question in question_string:
            question_dict[question] = 0
        
        # Now iterate through the people of each group and tally up 
        # the questions
        for person in persons:
            for question in person:
                question_dict[question] += 1
                
        # Now go through the dict and see which question(s) everyone answered
        # Add each question that everyone answered to the count
        questions_more_than_1answers = 0
        for key in question_dict:
            answers = question_dict[key]
            if answers == len(persons):
                questions_more_than_1answers += 1
        group_counts_pt2.append(questions_more_than_1answers)
        group_count_sum_pt2 += questions_more_than_1answers
        
print(f"In part 2, the sum of these counts is {group_count_sum_pt2}")
        