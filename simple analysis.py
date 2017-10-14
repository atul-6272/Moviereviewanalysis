# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 14:19:32 2017

@author: ATUL
"""
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

imdb_data = pd.read_csv('movie_metadata.csv') 
print("Check For Any NULL Values in the Data")
print(imdb_data.shape)
#imdb_data.count()
imdb_data.info()

print("\n\n\n\n")
print("#Replace every NULL values with 0 \n")
imdb_data.fillna(value=0,axis=1,inplace=True)
imdb_data.info()
print("\n\n\n\n")

imdb_data = imdb_data.sort_values(by = 'gross', ascending = False) 
movie_title = imdb_data['movie_title'] 
imdb_data.drop(labels=['movie_title'], axis=1,inplace = True)
imdb_data.insert(0, 'movie_title', movie_title)
imdb_data.head()
print(imdb_data.head(500))




#top Movies
imdb_data['gross_pct'] = np.round(100 * imdb_data['gross']/imdb_data['gross'].sum(), 2)
top_10 = 100* imdb_data['gross'].iloc[:10].sum()/imdb_data['gross'].sum()
top_50 = 100* imdb_data['gross'].iloc[:50].sum()/imdb_data['gross'].sum()
top_100 = 100* imdb_data['gross'].iloc[:100].sum()/imdb_data['gross'].sum()
top_200 = 100* imdb_data['gross'].iloc[:200].sum()/imdb_data['gross'].sum()
top_500 = 100* imdb_data['gross'].iloc[:500].sum()/imdb_data['gross'].sum()
top_movies = pd.Series(data = [top_10, top_50, top_100, top_200, top_500], index = ['top_10', 'top_50', 'top_100', 'top_200', 'top_500'])
print(top_movies.head())

#Director gross graph
director_gross = imdb_data.groupby('director_name')['gross'].sum()
director_gross = pd.DataFrame(director_gross)
director_gross = director_gross.sort_values(by = ['gross'], ascending = False)
director_gross[:10].plot(kind = 'bar')

# country wise movie
dist_countries_df = imdb_data.groupby(['country']).count()['imdb_score'].sort_values(ascending=False)[:10]

plt.figure(figsize=(8,4))
sns.barplot(y = dist_countries_df.index, x = dist_countries_df.values, palette = "PuBu_r")
plt.title('Countries that Release the Most Movies')
plt.xlabel('Movies Released')
plt.ylabel('Country')
plt.show()

#Top 10 IMDB Rating movies
df=imdb_data.loc[:,['movie_title','imdb_score','director_name','title_year']].sort_values(by = 'imdb_score', ascending = False)[:10]
print(df)

#IMDB RATING GRAPGH DISRTIBUTION
font = {'fontname':'Arial', 'size':'14'}
title_font = { 'weight' : 'bold','size':'16'}
labels=imdb_data["imdb_score"]
plt.hist(labels, bins=20)
plt.title("Distribution of the IMDB ratings")
plt.show()


