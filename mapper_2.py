#!/usr/bin/env python3

import sys
import os

#Input: Article}20160601 50

article_list = {}

for line in sys.stdin:
    line = line.strip()
    words = line.split('}')
    if len(words) < 2:
        continue
    split2 = words[1].split(' ')
    if len(split2) < 2:
        continue

    article = words[0]
    date = words[1].split(' ')[0]
    views = words[1].split(' ')[1]

    if int(views) < 10:
        continue

    if int(date) < 20160603:
        popularity = -1 * int(views)
    else:
        popularity = int(views)

    print(article + "\t" + date + "\t" + views + "\t" + str(popularity))