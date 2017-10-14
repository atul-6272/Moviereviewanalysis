# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 18:44:00 2017

@author: ATUL
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.options.display.max_columns = 100
pd.options.display.max_rows = 100


df = pd.read_csv("movie_metadata.csv")


def create_comparison_database(name, value, x, no_films):
    
    comparison_df = df.groupby(name, as_index=False)
    
    if x == 'mean':
        comparison_df = comparison_df.mean()
    elif x == 'median':
        comparison_df = comparison_df.median()
    elif x == 'sum':
        comparison_df = comparison_df.sum() 
    
    # Create database with either name of directors or actors, the value being compared i.e. 'gross',
    # and number of films they're listed with. Then sort by value being compared.
    name_count_key = df[name].value_counts().to_dict()
    comparison_df['films'] = comparison_df[name].map(name_count_key)
    comparison_df.sort_values(value, ascending=False, inplace=True)
    comparison_df[name] = comparison_df[name].map(str) + " (" + comparison_df['films'].astype(str) + ")"
   
    # create a Series with the name as the index so it can be plotted to a subgrid
    comp_series = comparison_df[comparison_df['films'] >= no_films][[name, value]][10::-1].set_index(name).iloc[:,0]
    
    return comp_series


fig = plt.figure(figsize=(18,6))

# Director_name
plt.subplot2grid((2,3),(0,0), rowspan = 2)
create_comparison_database('director_name','gross','sum', 0).plot(kind='barh', color='#006600')
plt.legend().set_visible(False)
plt.title("Total Gross of Director's Films")
plt.ylabel("Director (no. films)")
plt.xlabel("Gross (in billons)")

plt.subplot2grid((2,3),(0,1), rowspan = 2)
create_comparison_database('director_name','imdb_score','median', 4).plot(kind='barh', color='#ffff00')
plt.legend().set_visible(False)
plt.title('Median IMDB Score for Directors with 4+ Films')
plt.ylabel("Director (no. films)")
plt.xlabel("IMDB Score")
plt.xlim(0,10)

plt.tight_layout()



#ACTOR

fig = plt.figure(figsize=(18,6))

# Actor_1_name
plt.subplot2grid((2,3),(0,0), rowspan = 2)
create_comparison_database('actor_1_name','gross','sum', 0).plot(kind='barh', color='#006600', alpha=.8)
plt.legend().set_visible(False)
plt.title("Total Gross of Actor_1_name's Films")
plt.ylabel("Actor_1_name (no. films)")
plt.xlabel("Gross (in billons)")

plt.subplot2grid((2,3),(0,1), rowspan = 2)
create_comparison_database('actor_1_name','imdb_score','median', 8).plot(kind='barh', color='#ffff00', alpha=.8)
plt.legend().set_visible(False)
plt.title('Median IMDB Score for Actor_1_name with 8+ Films')
plt.ylabel("Actor_1_name (no. films)")
plt.xlabel("IMDB Score")
plt.xlim(0,10)

plt.tight_layout()