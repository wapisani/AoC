# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 00:48:40 2022

@author: wapisani
"""
import os

directory = r'F:\Documents\Programming\AoC\2022'
os.chdir(directory)

with open('input_day7.txt','r') as handle:
    data = handle.readlines()

# Part 1
dir_sizes = {}
pwd = ['/']
for line in data:  
    if 'dir ' in line or 'ls ' in line:
        continue
    
    line = line.strip('\n')    
    if 'cd' in line:
        if '..' in line:
            pwd.pop()
        else:
            directory = line.split(' ')[-1]
            pwd.append(directory)
            # tuples are hashable
            dir_sizes[tuple(pwd)] = 0
            
    elif line[0].isdigit():
        filesize = int(line.split(' ')[0])
        
        # This section adds the filesize to each parent directory.
        # Iteratively adds the filesize to each parent directory
        # Ex. pwd = ['/','asdf','lkjh','qwer']
        # dir_sizes[('/')] += filesize
        # dir_sizes[('/','asdf')] += filesize
        # Thanks to HackedServer for the solution: https://github.com/HackedServer/adventofcode/blob/mainline/2022/day_07.py
        for i in range(len(pwd)+1):
            filepath = tuple(pwd[:i]) 
            if filepath not in dir_sizes:
                dir_sizes[filepath] = filesize
            else:
                dir_sizes[filepath] += filesize
        

part1_total_size = 0
for size in dir_sizes.values():
    if size < 100000:
        part1_total_size += size
print(f"The sum of the total sizes of those directories with a size of at most 100000 is {part1_total_size}")


# Part 2
unused_space = 70000000 - dir_sizes[tuple(['/'])]
space_needed_to_free = 30000000 - unused_space

ideal_sized_directories = [] # space greater than space_needed_to_free
for size in dir_sizes.values():
    if size > space_needed_to_free:
        ideal_sized_directories.append(size)
        
print(f"The total size of the directory that, if deleted, would free up enough space on the filesystem to run the update is {min(ideal_sized_directories)}")
