import urllib
from BeautifulSoup import BeautifulSoup

url=raw_input('Enter - ')
html=urllib.urlopen(url).read()
soup=BeautifulSoup(html)

tags=soup('span')
s=0
for t in tags:
	 s=s+int(t.contents[0])
print s
