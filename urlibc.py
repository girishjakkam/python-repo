import urllib
fhand=urllib.urlopen('http://www.pythonlearn.com/code/intro-short.txt')
for line in fhand:
	print line
