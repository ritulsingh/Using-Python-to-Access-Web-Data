# -*- coding: utf-8 -*-
"""
Created on Fri May 15 16:44:02 2020

@author: Ritul Singh
"""
import json
import urllib.request as UR


url = input('Enter location: ')

count = 0

print('Retrieving', url)
xml = UR.urlopen(url).read()
print('Retrieved', len(xml), 'characters')

info = json.loads(xml)
for item in info["comments"]:
	
	number = int(item["count"])
	count = count + number
print (count)
