# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 19:25:46 2017

@author: ATUL
"""

import numpy as np  
import pandas as pd  
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import datasets, linear_model
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import PolynomialFeatures

df = pd.read_csv('movie_metadata.csv')
print(df.iloc[0])

#We clean the data and only select features which we plan to use. I selected some features which I thought might be having stronger influence on IMDB rating 
dfp = df[['title_year','movie_title','num_voted_users','budget','num_user_for_reviews','imdb_score']]
dfp = dfp.dropna(thresh=1)
dfp = dfp[(dfp.num_voted_users.notnull()) & (dfp.budget.notnull()) &(dfp.num_user_for_reviews.notnull())]
dfp = dfp[ (dfp.num_voted_users >= 1000) & (dfp.num_user_for_reviews > 50) & (dfp.imdb_score > 0)]
print(dfp.head(3))



#Only select the features we need. Then we split into training/test datasets. We also seperate out names of movies and year of release
features = dfp[['title_year','movie_title','num_user_for_reviews','num_voted_users']]
observations = dfp[['imdb_score']]

features_train, features_test,obs_train,obs_test = train_test_split(features,observations, test_size = 0.20,random_state=13)
movies_train = features_train[['movie_title','title_year']]
movies_test = features_test[['movie_title','title_year']]
features_train = features_train.drop('movie_title', 1).drop('title_year',1)
features_test = features_test.drop('movie_title', 1).drop('title_year',1)

#Lets run a LinearRegression with defaults. Output the RMS error , coefficients and intercept.
regr = linear_model.LinearRegression()
regr.fit(features_train, obs_train)
predictions = regr.predict(features_test.values) 
print('Coefficients: \n', regr.coef_)
print('Intercept: \n', regr.intercept_)
print("Mean squared error: %.2f" % np.mean((predictions - obs_test.values) ** 2))
print('Variance score: %.2f' % regr.score(features_test.values, obs_test.values))

print("----sample predictions -----")
for i in range(110,130):
    print( "{0} {1} -> predicted : {2:3.2f} \t actual {3}".format(movies_test[i-1:i].values[0][1],
           movies_test[i-1:i].values[0][0]
          ,predictions[i-1:i][0][0] 
          ,obs_test['imdb_score'][i-1:i].values[0]))



