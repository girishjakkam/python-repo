m={'jan':31,'Feb':60,'mar':91,'Apr':121,'May':152,'Jun':182,'Jul':213,'Aug':244,'Sept':274,'Oct':305,'Nov':335,'Dec':366}
f={'friday':1,'saturday':2,'sunday':3,'monday':4,'tuesday':5,'wednesday':6,'thursday':7}
u=raw_input("Enter a Day:")
print "%s/Jan/2016"%(f[u])
while f[u]<=366:
	f[u]=f[u]+7
	if f[u]<=m['jan']:	
		print "%s/Jan/2016"%(f[u])
	elif f[u]>=m['jan'] and f[u]<=m['Feb']:
		s=f[u]-m['jan']
		print "%s/Feb/2016"%(s)
	elif f[u]>=m['Feb'] and f[u]<=m['mar']:
		s=f[u]-m['Feb']
		print "%s/Mar/2016"%(s)
	elif f[u]>=m['mar'] and f[u]<=m['Apr']:
		s=f[u]-m['mar']
		print "%s/Apr/2016"%(s)
	elif f[u]>=m['Apr'] and f[u]<=m['May']:
		s=f[u]-m['Apr']
		print "%s/May/2016"%(s)
	elif f[u]>=m['May'] and f[u]<=m['Jun']:
		s=f[u]-m['May']
		print "%s/Jun/2016"%(s)
	elif f[u]>=m['Jun'] and f[u]<=m['Jul']:
		s=f[u]-m['Jun']
		print "%s/Jul/2016"%(s)
	elif f[u]>=m['Jul'] and f[u]<=m['Aug']:
		s=f[u]-m['Jul']
		print "%s/Aug/2016"%(s)
	elif f[u]>=m['Aug'] and f[u]<=m['Sept']:
		s=f[u]-m['Aug']
		print "%s/Sept/2016"%(s)
	elif f[u]>=m['Sept'] and f[u]<=m['Oct']:
		s=f[u]-m['Sept']
		print "%s/Oct/2016"%(s)
	elif f[u]>=m['Oct'] and f[u]<=m['Nov']:
		s=f[u]-m['Oct']
		print "%s/Nov/2016"%(s)
	elif f[u]>=m['Nov'] and f[u]<=m['Dec']:
		s=f[u]-m['Nov']
		print "%s/Dec/2016"%(s)	
		
		



	
