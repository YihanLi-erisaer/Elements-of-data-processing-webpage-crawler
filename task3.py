""" 
COMP20008 Semester 1
Assignment 1 Task 3
"""

from typing import Dict, List
import pandas as pd
import json
import requests
import bs4
import urllib
import unicodedata
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
#from task2 import task2
from task2 import preprocess_page, preprocess_text
from robots import process_robots, check_link_ok





# Task 3 - Producing a Bag Of Words for All Pages (2 Marks)
def task3(link_dictionary: Dict[str, List[str]], csv_filename: str):
    # link_dictionary is the output of Task 1, it is a dictionary
    # where each key is the starting link which was used as the 
    # seed URL, the list of strings in each value are the links 
    # crawled by the system. The output should be a csv which
    # has the link_url, the words produced by the processing and
    # the seed_url it was crawled from, this should be output to
    # the file with the name csv_filename, and should have no extra
    # numeric index.
    # Implement Task 3 here
    rows = []

    for seed_url, links in link_dictionary.items():
        for link_url in links:
            #result = task2(link_url, None)
            result = preprocess_page(link_url)
            words = result[link_url]
            #print(link_url)
            wordss = " ".join(words)
            #wordss = " ".join(result)
            rows.append((link_url, wordss, seed_url))
    dataframe = pd.DataFrame(rows, columns=['link_url', 'words', 'seed_url'])
    dataframe = dataframe.sort_values(['link_url', 'seed_url'])
    dataframe.to_csv(csv_filename, index=False)


    return dataframe
