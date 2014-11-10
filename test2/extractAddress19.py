#!/usr/bin/env python
#-*-coding:utf-8-*-
#
#Author:Weilong Guo
#指定される住所を変換する	

import sys
import codecs
import re

f = codecs.open("tweet.txt","r","utf-8")

pattern = re.compile(ur"(.*)((都|道|府|県)(.*)(市|県|区))")
for line in f:
   match = pattern.search(line)
   if match:
      print line.strip()






# u"(都|道|府|県)(.*)(市|県|区)" u"仙台市.*区"
