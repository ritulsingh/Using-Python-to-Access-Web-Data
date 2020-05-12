# -*- coding: utf-8 -*-
"""
Created on Tue May 12 16:32:46 2020

@author: Ritul Singh
"""

import urllib
from bs4 import BeautifulSoup

url = input('http://py4e-data.dr-chuck.net/comments_383954.html')

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
tag = soup("span")
count=0
sum=0
for i in tag:
	x=int(i.text)
	count+=1
	sum = sum + x
print (count)
print (sum)