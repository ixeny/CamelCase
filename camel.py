#!/usr/bin/env python
import sys
def camel(str):
 s=""
 for i in str.split():
  s=s+i.capitalize()
 print(s)
camel(sys.argv[1])

