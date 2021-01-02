#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 01:01:10 2020

@author: michaelnana
"""

"""mapper.py"""

import sys

# input for this step comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # split the line and select the two columns needed
    items = line.split(',')
    print('%s\t %s \t %s' % (items[3].upper(), items[0].upper(), items[2]))