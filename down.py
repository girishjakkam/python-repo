#!/usr/bin/python
# HTTP Header
print 'Content-Type:application/octet-stream; name="foo.txt"'
print 'Content-Disposition: attachment; filename="foo.txt"'
print
# Actual File Content will go hear.
fo = open("foo.txt", "rw+")
str = fo.read();
print str
# Close opend file
fo.close()
