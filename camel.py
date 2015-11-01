#!/usr/bin/env python
import sys
def camel(str):
 s=""
 for i in str.split():
  s=s+i.capitalize()
 print(s)
if len(sys.argv) > 1:
 s=""
 for i in range(1,len(sys.argv)):
  s=s+" "+sys.argv[i]
 camel(s)
else:
 print("usage: ./camel.py \"string\"")
