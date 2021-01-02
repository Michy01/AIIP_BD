#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 01:19:14 2020

@author: michaelnana
"""

"""reducer.py"""
import sys

current_tuple = None
current_grade = 0

count_grade = 0
tupl = None  # exple de tuple (math, jean)

top5 = []

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    
    # parse the input we got from mapper.py splitting by '\t'
    course, name, grade = line.split('\t')
    tupl=(course, name)
    # convert value (currently a string) to int
    try:
        grade = float(grade)
    except ValueError:
        # ignore/discard this line if value wasn't a number
        continue
    if current_tuple == tupl:
        current_grade += grade
        count_grade  += 1 
    else:
        if current_tuple:
            # write result to STDOUT
            avg = current_grade/count_grade
            if len(top5) < 5:
                couple = (current_tuple[1],  avg)
                top5.append(couple) # top5 = [(jean, 12/3), (paul, 13/2),....]
            else:
                top5.sort(key = lambda e : e[1])
                if avg > top5[0][1]:   
                    top5[0] = (current_tuple[1],  avg)
            if current_tuple[0] != tupl[0]: 
                print('%s\t%s' % (current_tuple[0], top5))
        current_grade = grade
        count_grade = 1
        current_tuple = tupl
        
if current_tuple:
    # write result to STDOUT
    avg = current_grade/count_grade
    if len(top5) < 5:
        couple = (current_tuple[1],  avg)
        top5.append(couple) # top5 = [(jean, 12/3), (paul, 13/2),....]
    else:
        top5.sort(key = lambda e : e[1])
        if avg > top5[0][1]:   
            top5[0] = (current_tuple[1],  avg)
    print('%s\t%s' % (current_tuple[0], top5))