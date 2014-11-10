#!/usr/bin/python
#
#Author:Weilong Guo
#

import sys
import codecs
import re

fileOpen = codecs.open("tweet.txt","r","utf-8")

patten = re.compile(u".なう$")

for line in f:
	match = pattern.search(line)
	if match:
		print line:
