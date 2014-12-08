#!/usr/bin/env python
#-*-coding:utf-8-*-
#
#Author:Weilong Guo

from stemming.porter2 import stem

for line in open("medline_1.txt"):
	line2 = line.strip().split("\t")
	print (line2[0]+"\t"+line2[1]+"\t"+stem(line2[1]))
