#!/usr/bin/env python
#-*- coding:utf8 -*-

#
#Author:Weilong Guo
#

import sys
import MeCab
import re
import codecs

f = codecs.open("japanese.txt","r","utf-8")
japanese = f.read()
m = MeCab.Tagger()
lines = m.parse(japanese.encode("utf-8")).split("\n");
dict = {}
for line in lines:
	if "\t"in line:
		tab_split = line.split("\t")
		comma_split = tab_split[1].split(",")
		dict[tab_split[0]] + " " + comma_split[6] + " " + comma_split[0] + " " + comma_split[1]] = tab_split[0]
	else:
		break

for k,v in dict.items():
	print "key: "+ k +"\t" + "value:" +v 

