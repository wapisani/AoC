# -*- coding: utf-8 -*-
"""
@author: wapisani
"""

import os
directory = r'F:\Documents\Programming\AoC\2021'
os.chdir(directory)

with open('input_day8.txt','r') as handle:
    data = [line.strip() for line in handle.readlines()]
   

# with open('sample_day8.txt','r') as handle:
#     data = [line.strip() for line in handle.readlines()]
    
signal_values = [value.split(' | ')[0] for value in data]    
output_values = [value.split(' | ')[1] for value in data]    
    
### Part 1 ###

digit_count = [0,0,0,0,0,0,0,0,0,0]
remaining_unknowns = []
segment_dict = {1: [], 4: [], 7: [], 8: []}
for output in output_values:
    values = output.split(' ')
    for value in values:
        if len(value) == 2:
            digit_count[1] += 1
            segment_dict[1].append(value)
        elif len(value) == 4:
            digit_count[4] += 1
            segment_dict[4].append(value)
        elif len(value) == 3:
            digit_count[7] += 1
            segment_dict[7].append(value)
        elif len(value) == 7:
            digit_count[8] += 1
            segment_dict[8].append(value)
        else:
            remaining_unknowns.append(value)
print(f'The digits 1, 4, 7, or 8 appear {sum(digit_count)} times.')

### Part 2 ###
signal_maps_list = []
unknowns_list = []
decoded_output = []
for i,signal in enumerate(signal_values):
    signals = signal.split(' ')
    sig_map = {}
    unknowns = []
    for sig in signals:
        sig = ''.join(sorted(sig))
        if len(sig) == 2:
            sig_map[1] = sig
        elif len(sig) == 4:
            sig_map[4] = sig
        elif len(sig) == 3:
            sig_map[7] = sig
        elif len(sig) == 7:
            sig_map[8] = sig
        else:
            unknowns.append(sig)
    # Now figure out what the rest of the unknown signals correspond to
    five_six = []
    two = []
    for unknown in unknowns:
        right_sides = sig_map[1]
        # Now figure out which of the unknowns is 2, 5, or 6
        
        if right_sides[0] in unknown and right_sides[1] not in unknown:
            five_six.append(unknown)
        elif right_sides[1] in unknown and right_sides[0] not in unknown:
            two.append(unknown)
     
    # It's possible that the five and six and two arrays are mixed up
    # so make sure that they're right. Only two will have the top-right line
    # while five and six both have the bottom-right
    if len(two) == 2:
        five_six, two = two,five_six
    
    sig_map[2] = two[0]
    unknowns.pop(unknowns.index(two[0]))
    # Six will be the longer string in five_six
    for sig in five_six:
        if len(sig) == 6:
            sig_map[6] = sig
            unknowns.pop(unknowns.index(sig))
        else:
            sig_map[5] = sig
            unknowns.pop(unknowns.index(sig))
    
    # The last five length string is 3
    for unknown in unknowns:
        if len(unknown) == 5:
            sig_map[3] = unknown
            
    unknowns.pop(unknowns.index(sig_map[3]))
        
    # Now just 0 and 9 to figure out
    # 0 does not have the middle line segment in 4 while 9 does
    for unknown in unknowns:
        for lines in sig_map[4]:
            if lines not in unknown:
                sig_map[0] = unknown
    unknowns.pop(unknowns.index(sig_map[0]))
    sig_map[9] = unknowns[0]
    # Append sig_map dictionary to list
    unknowns_list.append(unknowns)
    signal_maps_list.append(sig_map)
    
    rev_sig_map = {}
    rev_sig_map[sig_map[0]] = '0'
    rev_sig_map[sig_map[1]] = '1'
    rev_sig_map[sig_map[2]] = '2'
    rev_sig_map[sig_map[3]] = '3'
    rev_sig_map[sig_map[4]] = '4'
    rev_sig_map[sig_map[5]] = '5'
    rev_sig_map[sig_map[6]] = '6'
    rev_sig_map[sig_map[7]] = '7'
    rev_sig_map[sig_map[8]] = '8'
    rev_sig_map[sig_map[9]] = '9'
    
    # Now decode output
    output = output_values[i].split(' ')
    decoded = ''
    for value in output:
        value = ''.join(sorted(value))
        decoded += rev_sig_map[value]
    decoded_output.append(int(decoded))
    
print(f'The result of adding up all of the output values is {sum(decoded_output)}')