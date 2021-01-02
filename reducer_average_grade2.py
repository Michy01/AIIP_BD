#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 01:09:14 2020

@author: michaelnana
"""

"""reducer.py"""

# Find the average grade for each course

import sys
#import csv

current_course = None
current_grade = 0
course_count = 0
key = None

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    
    # parse the input we got from mapper.py splitting by '\t'
    course, _, grade = line.split('\t')
    #course = key.split("\t")[1]
    # convert value (currently a string) to int

    try:
        grade = float(grade)
    except ValueError:
        # ignore/discard this line if value wasn't a number
        continue
        
    #Since during the shuffling phase outputs from the mappers
    #are sorted before passed to the reduce we can safely
    #stop counting a particular key after the last occurance
    
    if current_course == course:
        current_grade += grade
        course_count += 1
    else:
        if current_course:
            # write result to STDOUT
            print('%s\t%s' % (current_course, current_grade/course_count))
        current_grade = grade
        course_count = 1
        current_course = course
# ensure the results for the last key is written to STDOUT
if current_course == course:
    print('%s\t%s' % (current_course, current_grade/course_count))

