
name = raw_input("Enter file:")
handle = open(name)
lst=list()
z=list()
new=dict()
counts=dict()
for line in handle:   
	line.split()
	if line.startswith('From')==True:
        	pos1=line.find(':')
		lst.append(line[pos1-2:pos1])
		
			
			

for name in lst:
	if not name == "om":
		counts[name]=counts.get(name,0)+1




for c,w in sorted(counts.items()):
	print c,w
