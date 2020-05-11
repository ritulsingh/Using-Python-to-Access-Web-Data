# -*- coding: utf-8 -*-
"""
Created on Sun May 10 17:00:14 2020

@author: Ritul Singh
"""

import re
hand = open('realdata.txt')
numlist = list()
for line in hand:
	stuff = sum(re.findall('[0-9]+',line))
	numlist = numlist + stuff
sum=0
for z in numlist:
    sum = sum + int(z)
print(sum)