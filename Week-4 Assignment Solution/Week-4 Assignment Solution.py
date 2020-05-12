# -*- coding: utf-8 -*-
"""
Created on Tue May 12 16:32:46 2020

@author: Ritul Singh
"""

from urllib import request
from bs4 import BeautifulSoup
html=request.urlopen('http://py4e-data.dr-chuck.net/comments_383954.html').read()
soup = BeautifulSoup(html)
tags=soup('span')
sum=0
for tag in tags:
    sum=sum+int(tag.contents[0])
print(sum)
