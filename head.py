import httplib
conn = httplib.HTTPSConnection("www.python.org")
conn.request("HEAD","/")
res = conn.getresponse()
print res.status, res.reason

data = res.read()
print len(data)
print data
data == ''
