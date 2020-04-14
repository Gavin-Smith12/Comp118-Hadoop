#!/usr/bin/env python3

import sys
import os

article_list = {}

for line in sys.stdin:
    words = line.split()
    article = words[0].split('}')[0]
    date = words[0].split('}')[1]
    views = words[1]

    if int(views) < 10:
        continue

    if article in article_list:
        article_list[article]["date"].append(date)
        article_list[article]["views"].append(views)
    else:
        article_list[article] = {"name":article, "date":[date], "views":[views]}

for page in article_list:
    #print(f"{article['name']} {article['date']} {article['views']}")
    print(article_list[page]["name"] + " " + str(article_list[page]["date"]) + " " + str(article_list[page]["views"]))