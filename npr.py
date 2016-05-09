import os
gary= os.popen('cat /etc/services').read()

def P_list(gary):
	pnum=[]
	plist=gary.split()
	for i in plist:
		for p in i:
			
			if p == "/" :
				pnum.append(i)
	return pnum	


l=[]
for i in P_list(gary):
	for n in i:
		if (n=="p"):
				l.append(i)
	
no=l[15::]
num1=[]
num2=[]
for i in no:
	num1.append(i.replace("/tcp",""))
for i in num1:
	num2.append(i.replace("/udp",""))
	
print num2


