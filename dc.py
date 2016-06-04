
name = raw_input("Enter file:")
handle = open(name)
lst=list()
z=list()
counts=dict()
for line in handle:   
	line.split()
	if line.startswith('From')==True:
        	pos=line.find('From')
		pos1=line.find('@')
		lst.append(line[pos+5:pos1+9])
			

for name in lst:
	counts[name]=counts.get(name,0)+1

bigword=None
bigcount=None
for word,count in counts.items():
	if bigcount is None or count>bigcount:
		bigword=word
		bigcount=count
print bigword,bigcount		
