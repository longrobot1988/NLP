#!/usr/bin/env python
#-*- coding:utf8 -*-

#
#Author:Weilong Guo
#

import sys

count = {}
for line in open("medline_bigram.txt","r"):
	bigram = line.strip()
	if bigram  not in count:
		count[bigram] = 1
	else:
		count[bigram] += 1

output = open("medline_bigram_count.txt","w")
for i,j in count.items():
	print str(j) + "\t" + i 
	output.write(str(j) + "\t" + i + "\n")
