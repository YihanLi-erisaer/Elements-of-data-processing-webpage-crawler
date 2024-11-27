""" 
COMP20008 Semester 1
Assignment 1 Task 1
"""
import pandas as pd
import pandas as pd
import json
from typing import Dict, List
from bs4 import BeautifulSoup
import requests
import bs4
import urllib
from robots import process_robots, check_link_ok
import urllib.robotparser
from lxml import etree
import re
from urllib.parse import urljoin

# A simple page limit used to catch procedural errors.
SAFE_PAGE_LIMIT = 1000


# Task 1 - Get All Links (3 marks)
def find_page(link, page_visited):
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')

    robot_rules = process_robots(response.text)

    links = soup.findAll('a')

    pattern = link.split('/')[3]
    
    pattern1 = "/" + pattern + "/"

    seed_link = soup.findAll('a', href=re.compile(r"^" + pattern1))

    to_visit = []
    for link1 in seed_link:
        if page_visited == SAFE_PAGE_LIMIT:
            break

        if not check_link_ok(robot_rules, link1['href']):
            continue
        to_visit.append(urljoin(link, link1['href']))
    return to_visit





def task1(starting_links: List[str], json_filename: str) -> Dict[str, List[str]]:
    # Crawl each url in the starting_link list, and output
    # the links you find to a JSON file, with each starting
    # link as the key and the list of crawled links for the
    # value.
    # Implement Task 1 herelink_dict = {}
    pages = {}
    for link in starting_links:
        links_in_page = []
        page_visited = 1
        links_in_page = find_page(link, page_visited)

        if page_visited == SAFE_PAGE_LIMIT:
            break
        for link_extra in links_in_page:
            if link_extra == link:
                continue
            else:
                for link1 in find_page(link_extra, page_visited):
                    if link1 not in links_in_page:
                        links_in_page.append(link1)
        page_visited += 1
        pages[link] = links_in_page

    # Write the pages dictionary to the output file in JSON format
    with open(json_filename, "w") as f:
        json.dump(pages, f)


    return pages

