#!/usr/bin/python

#
# Author Weilong Guo
#


import sys


fs = open(sys.argv[1],"r")
add = {}


for line in fs:
    words = line.split("\t")
    add[words[0]] = words[1]


for i,j in sorted(add.items(),key = lambda add:(add[0],add[1])):
    print i,j

