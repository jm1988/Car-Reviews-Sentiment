# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 10:59:12 2020

@author:  Juan Marte
"""
import os
from bs4 import BeautifulSoup
import pandas as pd

df = pd.DataFrame()



for yf in ['2007','2008','2009']:
    
    file_list = os.listdir(os.getcwd()+'\\cars\\' + yf)
    for f in file_list:
        with open('cars/'+yf+'/' + f, 'rb') as file:  
            data = file.read() 
        
        soup = BeautifulSoup(data, features="lxml")
        title = []
        date = []
        author = []
        review = []
        
        for i in range(len(soup.findAll('doc'))):
            title.append(str(file).split(' ')[1].replace("name='cars/",''))
            try:
                date.append(soup.findAll('doc')[i].find('date').text)
            except:
                date.append('none')
            try:
                author.append(soup.findAll('doc')[i].find('author').text)
            except:
                author.append('none')
            try:
                review.append(soup.findAll('doc')[i].find('text').text)
            except:
                review.append('none')        
        
        dat = pd.DataFrame({'title':title,
                           'date':date,
                           'author':author,
                           'review':review})
        df = df.append(dat)
    
df.to_csv('cars_r.csv', index=False)

