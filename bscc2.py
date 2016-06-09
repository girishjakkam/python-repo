import urllib
from BeautifulSoup import BeautifulSoup
lst=list()
url=raw_input('Enter - ')
i=0
while i<8:
	html=''
	print url
	html=urllib.urlopen(url).read()
	soup=BeautifulSoup(html)
	tags=soup('a')	
	for tag in tags:
		lst.append(tag.get('href',None))
	url=lst[17]
	lst=[]
	i+=1
	
	
	

