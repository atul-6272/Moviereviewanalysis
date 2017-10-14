# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 18:34:43 2017

@author: ATUL
"""

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('movie_metadata.csv')
df.head()

'''keys = np.sort(df.columns)
maxKeyLength = max(map(lambda x: len(x), keys))
print('number of keys: %s\n\n' % len(keys))
for i, key in enumerate(keys):
    print(('•{:%s}' % (maxKeyLength)).format(key), end = ' ')
    if i % 4 == 3:
        print('\n')
        
'''

df_genre = pd.DataFrame(columns = ['genre', 'cgenres', 'budget', 'gross', 'year'])
df_clean = df[['budget', 'genres', 'gross', 'title_year']].dropna()
def genreRemap(row):
    global df_genre
    d = {}
    genres = np.array(row['genres'].split('|'))
    n = genres.size
    d['budget'] = [row['budget']]*n
    d['gross'] = [row['gross']]*n
    d['year'] = [row['title_year']]*n
    d['genre'], d['cgenres'] = [], []
    for genre in genres:
        d['genre'].append(genre)
        d['cgenres'].append(genres[genres != genre])
    df_genre = df_genre.append(pd.DataFrame(d), ignore_index = True)

df_clean.apply(genreRemap, axis = 1)
df_genre['year'] = df_genre['year'].astype(np.int16)
df_genre = df_genre[['genre', 'budget', 'gross', 'year', 'cgenres']]

df_genre.head(10)
print(df_genre.head(10))



genre_count = df_genre['genre'].value_counts().sort_index()
df_gCount = pd.DataFrame({'genre': genre_count.index, 'count': genre_count.values})
f, ax = plt.subplots(figsize = (8, 5))
sns.barplot(x = 'count', y = 'genre', data = df_gCount)
ax.set_title('.: occurences per genre :.')
ax.set_xlabel('occurrences')
ax.set_ylabel('genres')