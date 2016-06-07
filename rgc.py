import re
lst=list()
name = raw_input("Enter file:")
handle = open(name)
for n in handle:
	x=re.findall('[0-9]+',n)
	if x != []:
		lst.append(x)
s=[]
for i in lst:
	s=s+i

e=0
for w in s:
	e=e+int(w)
print e
