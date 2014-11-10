#!/usr/bin/python
#_*_ coding:utf-8 _*_
#Author:Weilong Guo
#

import sys
import codecs
import re

fileOpen = codecs.open("tweet.txt","r","utf-8")

pattern = re.compile(u".なう$")

for line in fileOpen:
	match = pattern.search(line)
	if match:
		print line.strip()