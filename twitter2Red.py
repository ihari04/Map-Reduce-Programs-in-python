#!/usr/bin/env python
#Takes key value pairs from Map and sums it by Key. Produces totals by day of the week

import sys
import string

result = 0
keydict = dict()
for line in sys.stdin:
  (key,val) = line.strip().split('\t',1)
#  result = result + int(val)
  keydict[key] = keydict.get(key,0)+ int(val)

#print '%s\t%s' % (key,str(result))
print keydict
