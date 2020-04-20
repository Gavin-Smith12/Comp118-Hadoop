#!/usr/bin/python3

import os
import sys

# date -> {}(ArticleTitle -> views)
days = {}

articles = {}

for line in sys.stdin:

    if line == "":
        continue
    # 
    line = line.strip()
    split = line.split('}')
    article = split[0]
    if len(split) < 2:
        continue
    split2 = split[1].split('\t')
    if len(split2) < 2:
        continue
    date = split[1].split('\t')[0]
    views = split[1].split('\t')[1]

    try:
        viewNum = int(views)
    except:
        continue

    # Current date in dictionary
    if date in days:
        # article was viewed that day
        if article in days[date]:
            days[date][article] += viewNum
        else:
            days[date][article] = viewNum
    else:
        days[date] = {article:viewNum}

for date in days:
    for article in days[date]:
        views = days[date][article]
        print(article + "}" + str(date) + " " + str(views))