#!/usr/bin/python
#_*_ coding:utf-8 _*_
#Author:Weilong Guo
#

import sys
import codecs
import re

fileOpen = codecs.open("tweet.txt","r","utf-8") #

pattern = re.compile(u".なう$") 
#日本語の入った文字はu''　のようにこの文字列がUTF-8が書かれている
#$が文字列の最後の直前にマッチする		


for line in fileOpen:
	match = pattern.search(line)
	if match:
		print line.strip()