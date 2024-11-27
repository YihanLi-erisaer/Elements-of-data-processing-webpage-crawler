"""
COMP20008 Semester 1
Assignment 1 Task 2
"""
import json
from bs4 import BeautifulSoup
import requests
import bs4
import urllib
import unicodedata
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

from robots import process_robots, check_link_ok
def preprocess_text(text):

   
    #text = text.casefold()

    text = unicodedata.normalize('NFKD', text.lower())

    #text = re.sub(r'\s+', ' ', text)

    text = re.sub(r'[^A-Za-z\\]', ' ', text)
    
    #text = re.sub(r'[^\w\s\\]', ' ', text)

    #text = re.sub(r'\b\w{1}\b', ' ', text)
    #tokens = text.split()
    tokens = [word for word in text.split(' ') if (len(word) > 1)]
    
    text = re.sub(r'\s+', ' ', text)

    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    #all_stopWords = set(stopwords.words('english'))
    #tokens = [x for x in tokens if not(x in all_stopWords)]

    stemmer = PorterStemmer()
    tokens = [stemmer.stem(token) for token in tokens]
    #tokens = [PorterStemmer().stem(token) for token in tokens]




    #pattern = re.compile(r'\d+')
    #tokens = [s for s in tokens if not pattern.search(s)]
    

    return tokens


def preprocess_page(url):
    try:

        response = requests.get(url)

        soup = BeautifulSoup(response.content, 'html.parser')


        for el in soup.select('th.infobox-label'):
            el.decompose()
        for el in soup.select('div.printfooter'):
            el.decompose()
        for el in soup.select('div#toc'):
            el.decompose()
        for el in soup.select('table.ambox'):
            el.decompose()
        for el in soup.select('div.asbox'):
            el.decompose()
        for el in soup.select('span.mw-editsection'):
            el.decompose()
        content = soup.select_one('div#mw-content-text').get_text(separator=' ', strip=True)


        tokens = preprocess_text(content)


        result = {url: tokens}

    except:
        result = {url: []}
    return result





# Task 2 - Extracting Words from a Page (4 Marks)
def task2(link_to_extract: str, json_filename: str):
    # Download the link_to_extract's page, process it 
    # according to the specified steps and output it to
    # a file with the specified name, where the only key
    # is the link_to_extract, and its value is the 
    # list of words produced by the processing.
    # Implement Task 2 here

    result = preprocess_page(link_to_extract)
    with open(json_filename, 'w') as outfile:
        json.dump(result, outfile)
