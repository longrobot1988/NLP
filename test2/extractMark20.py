#!/usr/bin/env python
#-*-coding:utf-8-*-

import sys
import codecs
import re

f = codecs.open("tweet.txt","r","utf-8")

pattern = re.compile(ur"(\b\(\W+\)\b)")

for line in f:
   match = pattern.search(line)
   if match:
      print match.group(1)






