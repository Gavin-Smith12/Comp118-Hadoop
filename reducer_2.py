#!/usr/bin/env python3

import sys
import os
import ast

# Modern_art [20160601, 20160609] [50,75] input
# Modern_art\t[20160609,20160601]\t[75,50]\t125\t25 output

article_list = {}

for line in sys.stdin:
    dates_to_views = {}

    line = line.strip()
    words = line.split('\t')
    if len(words) < 4:
        continue
    article = words[0]
    date = words[1]
    views = words[2]
    popularity = int(words[3])

    if article in article_list:
        article_list[article]["date"].append(date)
        article_list[article]["views"].append(views)
        article_list[article]["total_views"] += int(views)
        article_list[article]["popularity"] += popularity
    else:
        article_list[article] = {"name":article, "date":[date], "views":[views], "total_views":int(views), "popularity":int(popularity)}

for article in article_list:

    dates = article_list[article]["date"]
    views = article_list[article]["views"]

    # maps dates to number of views
    for i in range(0,len(dates)):
        dates_to_views[int(dates[i])] = int(views[i])
        dates[i] = int(dates[i])
    
    # dates is sorted
    dates.sort()

    # views is ordered
    ordered_views = []
    for i in range(0, len(dates)):
        ordered_views.append(dates_to_views[dates[i]])

    print(article + "\t" + str(dates) + "\t" + str(ordered_views) + "\t" + str(article_list[article]["total_views"]) + "\t" + str(article_list[article]["popularity"]))
