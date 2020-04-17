#!/usr/bin/env python3

import sys
import os
import ast

# Modern_art [20160601,20160609] [50,75] input
# Modern_art\t[20160609,20160601]\t[75,50]\t125\t25 output

for line in sys.stdin:
    dates_to_views = {}

    words = line.split()
    article = words[0]
    dates = ast.literal_eval(words[1])
    views = ast.literal_eval(words[2])
    
    # maps dates to number of views
    for i in range(0,len(dates)):
        dates_to_views[int(dates[i])] = int(views[i])
        dates[i] = int(dates[i])
    
    # dates is sorted
    dates.sort()

    first_half = 0
    second_half = 0

    # views is ordered
    ordered_views = []
    for i in range(0, len(dates)):
        ordered_views.append(dates_to_views[dates[i]])
        if dates[i] < 20160603:
            first_half += dates_to_views[dates[i]]
        else:
            second_half += dates_to_views[dates[i]]

    print(article + "\t" + str(dates) + "\t" + str(ordered_views) + "\t" + str(sum(ordered_views)) + "\t" + str(second_half - first_half))
