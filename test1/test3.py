#!/usr/bin/python
#-*- coding: utf8 -*-

import sys

fs0 = open(sys.argv[1],"r")
fs1 = open("col1.txt","w")
fs2 = open("col2.txt","w")

for line in fs0:
	words = line.split("\t")
	#print words
	fs1.write(words[0].strip() + "\n")
	fs2.write(words[1].strip() + "\n")

fs1.close
fs2.close

