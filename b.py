#!/usr/bin/python
import sys,os

a,b=os.popen2('./a.py',bufsize=0)
for line in b:
    print line,
    sys.stdout.flush()
