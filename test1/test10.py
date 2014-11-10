#!/usr/bin/python
#
# Author Weilong Guo
#


import sys


fs = open(sys.argv[1],"r")
add = {}


for line in fs:
    words = line.split("\t")
    if words[0] not in add:
        add[words[0]] = 1
    else:
        add[words[0]] += 1
        
for i,j in sorted(add.items(),key = lambda add: add[1],reverse = True):
    print i,j

