# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('tr')
for tag in tags:
    tag.split()
    # Look at the parts of a tag
    print 'TAG:',tag
    pos=tag.find('class')
    print pos
