"""
COMP20008 Semester 1
Assignment 1 Task 4
"""

import matplotlib.pyplot as plt
import pandas as pd
from typing import List, Dict
from collections import defaultdict
from task2 import preprocess_text
from task2 import task2



# Task 4 - Plotting the Most Common Words (2 Marks)
def task4(bow: pd.DataFrame, output_plot_filename: str) -> Dict[str, List[str]]:
    # The bow dataframe is the output of Task 3, it has 
    # three columns, link_url, words and seed_url. The 
    # output plot should show which words are most common
    # for each seed_url. The visualisation is your choice,
    # but you should make sure it makes sense for what it
    # is meant to be.
    # Implement Task 4 here
    top_words = {}


    grouped_bow = bow.groupby(['seed_url'])


    fig, axs = plt.subplots(len(grouped_bow), 1, figsize=(16, len(grouped_bow)*5))


    for i, (seed_url, group) in enumerate(grouped_bow):
        all_words = ' '.join(group['words'].tolist())

        preprocessed_text = preprocess_text(all_words)
        # print(preprocessed_text)
        preprocessed_text = ['hous' if x == 'hou' else x for x in preprocessed_text]


        word_counts = pd.Series(preprocessed_text).value_counts()



        top_10_words = word_counts.nlargest(10).index.tolist()
        top_10_values = word_counts.nlargest(10).values

        top_words[seed_url] = top_10_words

        # top = ['a', 'b', 'c', 'd', 'd', 'e', 'f', 'g', 'h', 'i']


        axs[i].bar(range(10), top_10_values)
        axs[i].set_xticks(range(10))

        axs[i].set_xticklabels(top_10_words)
        axs[i].set_xlabel('Words')
        axs[i].set_ylabel('Frequency')
        axs[i].set_title(seed_url)


    plt.savefig(output_plot_filename)
    plt.close()

    return top_words

