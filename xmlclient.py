import xmlrpclib

s = xmlrpclib.ServerProxy('http://localhost:9541')
print s.pow(2,10)  # Returns 2**3 = 8
print s.add(2,3)  # Returns 5
print s.div(5,2)  # Returns 5//2 = 2
print s.mul(2,5)

# Print list of available methods
print s.system.listMethods()