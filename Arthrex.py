# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 11:37:58 2017

@author: lli
"""

"""
This script grab all product from Arthrex.com and gether all info into a DataFrame
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import pandas as pd


html=urlopen("https://www.arthrex.com/knee/products")
soup=BeautifulSoup(html)
R1=soup.findAll('h5',{"class":"product-group h-bar collapsible clearfix collapsed"})

data=pd.DataFrame(columns=['Product Number', 'Description'])
count=0

for url in soup.findAll("a",attrs={"class":"product-group-link pull-left"}):
    R2=url.get('href')
    try:
        Hlist=urlopen("https://www.arthrex.com"+R2)
        bsoup=BeautifulSoup(Hlist)
        for info in bsoup.findAll('a',{"class":"product-label"}):
             data.set_value(count, 'Product Number', info.get('href'))
        for info in bsoup.findAll('a',{"class":"product-label"}):
             string=info.find('span')
             data.set_value(count, 'Description', string.text)
    except HTTPError as e:
        print('This link does not work')
    count+=1