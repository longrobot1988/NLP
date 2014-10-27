#!/usr/bin/python
#
# Author Weilong Guo
#

import sys
import locale


fs = open(sys.argv[1],"r")
col1 = []


for line in fs:
    words = line.split("\t")
    col1.append(words[0])
    

for i in sorted(col1):
    print  i
