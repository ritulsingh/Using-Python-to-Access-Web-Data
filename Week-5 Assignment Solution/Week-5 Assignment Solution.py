# -*- coding: utf-8 -*-
"""
Created on Wed May 13 14:47:03 2020

@author: Ritul Singh
"""
import urllib.request as UR
import xml.etree.ElementTree as ET

url = input('Enter location: ')
# 'http://python-data.dr-chuck.net/comments_42.xml'

total_number = 0
sum = 0

print('Retrieving', url)
xml = UR.urlopen(url).read()
print('Retrieved', len(xml), 'characters')

tr = ET.fromstring(xml)
count = tr.findall('.//count')
for item in count:
    sum += int(item.text)
    total_number += 1

print('Count:', total_number)
print('Sum:', sum)

# Enter location: http://py4e-data.dr-chuck.net/comments_383956.xml
# Retrieving http://py4e-data.dr-chuck.net/comments_383956.xml
# Retrieved 4203 characters
# Count: 50
# Sum: 2542
