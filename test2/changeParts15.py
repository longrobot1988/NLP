#!/usr/bin/env python
#_*_coding:utf-8 _*__
#
#Author:Weilong Guo
#指定される部分を交換する		

import sys
import codecs
import re

fileOpen = codecs.open("tweet.txt","r","utf-8")

pattern = re.compile(u"(@)(.+?)(\W)")

for line in fileOpen:
   match = pattern.search(line)
   if match:
      s = match.group(2)
      l = line.replace(s,"<a href=\"https://twitter.com/#!/"+s+"\">@"+s+"</a>")
      print line.strip()
