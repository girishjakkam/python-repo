import xml.etree.ElementTree as ET
import urllib
p=0
url=raw_input('Enter - ')
n=urllib.urlopen(url).read()
s=ET.fromstring(n)
c=s.find('comments')
for i in c:
	p=p+int(i.find('count').text)
print p
