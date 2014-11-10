#!/usr/bin/env python
#_*_coding:utf-8 _*__
#
#Author:Weilong Guo
#住所を抽出せよ		

import sys
import codecs
import re

f = codecs.open("tweet.txt","r","utf-8")

pattern = re.compile(u"仙台市.*区")
for line in f:
   match = pattern.search(line)
   if match:
      print line.strip()
