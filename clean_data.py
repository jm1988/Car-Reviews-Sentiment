# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 12:42:16 2020

@author: Juan Marte
"""

import pandas as pd
import numpy as np
from textblob import TextBlob

df = pd.read_csv('cars_r.csv')

#remove observation with missing date and author
df = df.loc[df['date']!='none']

#print(df['title'][0].replace("'>",'').split('/')[1])

#remove the folder name from title
df['title'] = df['title'].str.replace("'>",'').str.split('/', expand=True)[1]

#Creating car make, model and year columns
df['car_year'] = df['title'].str.split('_', expand=True)[0]
df['car_make'] = df['title'].str.split('_', expand=True)[1]
df['car_model'] = df['title'].str.split('_', expand=True)[2]

#Creating new column with review length
df['review_lenght'] = df['review'].apply(len)

#Number of words on review
df['words_count'] = df['review'].apply(lambda x: len(x.split()))


df['date'] = pd.to_datetime(df['date'])

#Create columns with common words
df['comfort'] = np.where(df['review'].apply(lambda x: 'comfort' in x.lower()),1,0)
df['power'] = np.where(df['review'].apply(lambda x: 'power' in x.lower()),1,0)
df['problem'] = np.where(df['review'].apply(lambda x: 'problem' in x.lower()),1,0)
df['quiet'] = np.where(df['review'].apply(lambda x: 'quiet' in x.lower()),1,0)
df['speed'] = np.where(df['review'].apply(lambda x: 'speed' in x.lower()),1,0)
df['noise'] = np.where(df['review'].apply(lambda x: 'noise' in x.lower()),1,0)
df['great'] = np.where(df['review'].apply(lambda x: 'great' in x.lower()),1,0)


#Working with text data:

# Adding a column for the polarity of the review
df['review_polarity'] = df['review'].apply(lambda x: TextBlob(x).polarity)

# Adding a column for the subjectivity of the review
df['review_subjectivity'] = df['review'].apply(lambda x: TextBlob(x).subjectivity)

# Clasifying the polarity
def feeling(x):
    if x < 0:
        return 'negative'
    elif x == 0:
        return 'neutral'
    elif x > 0:
        return 'positive'
    else:
        return None

df['pol_class'] = df['review_polarity'].apply(feeling)
df.drop(['author','review'], axis=1, inplace=True)

df.to_csv('post_clean_data.csv', index=False)

