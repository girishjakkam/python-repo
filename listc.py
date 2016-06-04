fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    line=line.rstrip()
    words=line.split()
    for n in words:
	if n not in lst:
		lst.append(n)
    			
            
        
print lst
