"""
COMP20008 Semester 1
Assignment 1 Task 5
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from typing import Dict, Union, List

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import PCA
from sklearn.preprocessing import Normalizer  


# Task 5 - Dimensionality Reduction (3 marks)
def task5(bow_df: pd.DataFrame, tokens_plot_filename: str, distribution_plot_filename: str) -> Dict[str, Union[List[str], List[float]]]:
    # bow_df is the output of Task 3, for this task you 
    # should generate a bag of words, normalisation of the 
    # data perform PCA decomposition to 2 components, and 
    # then plot all URLs in a way which helps you answer
    # the discussion questions. If you would like to verify 
    # your PCA results against the sample data, you can return
    # the PCA weights - containing the list of most positive
    # weighted words, most negatively weighted words and the 
    # weights in the PCA decomposition for each respective word.
    # Implement Task 5 here


    vectorizer = CountVectorizer()
    bow = vectorizer.fit_transform(bow_df['words'])

    
    nbow = Normalizer(norm='max').fit_transform(bow)
    
    pca = PCA(n_components=2)
    pca_component = pca.fit_transform(nbow.toarray())
    
    token_list = vectorizer.get_feature_names_out()
    
    

    Dict = {}
    for index in range(2):
        component_weights = pca.components_[index]
        positive_indices = np.argsort(component_weights)[-10:]
        positive_tokens = [token_list[j] for j in positive_indices]
        positive_weights = component_weights[positive_indices]

        negative_indices = np.argsort(component_weights)[:10]
        negative_tokens = [token_list[j] for j in negative_indices]
        negative_weights = component_weights[negative_indices]

        Dict[str(index)] = {'positive': positive_tokens[::-1], 'negative': negative_tokens[::-1],
            'positive_weights': positive_weights[::-1].tolist(), 'negative_weights': negative_weights[::-1].tolist()}
    seed_url_list = bow_df['seed_url'].unique()

    fig, (ax1, ax2) = plt.subplots(1, 2) 
    fig.suptitle('Top 10 positive and Negative token plots')
    #print(seed_url_list[0])
    ax1.set_title(seed_url_list[0])
    ax1.barh(Dict['0']['positive'], Dict['0']['positive_weights'])
    ax1.barh(Dict['0']['negative'], Dict['0']['negative_weights'])

    ax2.set_title(seed_url_list[1])
    ax2.barh(Dict['1']['positive'], Dict['1']['positive_weights'])
    ax2.barh(Dict['1']['negative'], Dict['1']['negative_weights'])

    fig.tight_layout(pad = 5, h_pad= 5)

    fig.savefig(tokens_plot_filename)
    

    fig, ax = plt.subplots()
    for url in seed_url_list:
        data = pca_component[bow_df['seed_url'] == url]
        #print(data)
        ax.scatter(data[:, 0], data[:, 1], label = url)
        #print(data[:, 1])
    ax.legend()
    plt.savefig(distribution_plot_filename)

    
    return Dict


