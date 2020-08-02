# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 14:47:48 2020

@author: Juan Marte
"""

import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
from nltk.stem.wordnet import WordNetLemmatizer
import re



df = pd.read_csv('cars_r.csv')
df = df.loc[df['date']!='none']

other_words = ["I","It","n't","'s","The","the","This"]
stop_words = set(stopwords.words("english"))
all_reviews = " ".join(r for r in df['review'])
wt = word_tokenize(all_reviews)
clean_text = []
lem = WordNetLemmatizer()
#'hello467'.translate(None, '0123456789')
for w in wt:
    if w not in stop_words and w not in string.punctuation and w not in other_words:
        #The regex remove any number. All words are in lower case.
        clean_text.append(lem.lemmatize(re.sub(r'\d+','',w)).lower())        

cw = pd.DataFrame({'words':clean_text})    

cw['words'].value_counts().to_csv('word_count.csv')
        
# fdist = FreqDist(clean_text)
# print(fdist.most_common)