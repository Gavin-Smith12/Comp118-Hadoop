#!/usr/bin/env python3

import sys
import os
import urllib.parse

filepath = os.environ.get("map_input_file", "stdin")
date = os.path.split(filepath)[-1].split('-')[1]
excluded_words = ['Media', 'Special', 'Talk', 'User', 'User_talk', 
                  'Project', 'Project_talk', 'File', 'File_talk', 
                  'MediaWiki', 'MediaWiki_talk', 'Template', 
                  'Template_talk', 'Help', 'Help_talk', 'Category', 
                  'Category_talk', 'Portal', 'Wikipedia', 'Wikipedia_talk']

excluded_files = ['jpg', 'gif', 'png', 'JPG', 'GIF', 'PNG', 'ico', 'txt']

excluded_pages = ['404_error', 'Main_Page', 'Hypertext_Transfer_Protocol',
                  'Favicon.ico', 'Search']

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    project = words[0]
    article = urllib.parse.unquote_plus(words[1])
    views = words[2]

    if project != 'en':
        continue

    if article.split(':')[0] in excluded_words:
        continue

    if article[0].islower():
        continue

    if '.' in article:
        if article.split('.')[1] in excluded_files:
            continue

    if article in excluded_pages:
        continue

    print(article + "}" + date + " " + views)