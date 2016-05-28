#!/usr/bin/env python
#This program produces key value pairs (Day of the week, 1)

import json
import sys
import string
from pprint import pprint

#file = open('part-03212','r')
#data = file.read().splitlines()
#file.close()
#data = open('part-03212','r')

count = 0
#for line in data:
for line in sys.stdin:
  data1 = json.loads(line)
  name = data1['user']['screen_name'].lower()
  count = count + 1
  create = data1['created_at']
  day = create[0:3]
  if name == 'prezono':
    print '%s\t%s' % (day , str(1))
