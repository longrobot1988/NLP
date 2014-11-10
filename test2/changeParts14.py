#!/usr/bin/env python
#_*_coding:utf-8 _*__
#
#Author:Weilong Guo
#スイッターのユーザー名（＠で始まる文字列	）を抽出せよ

import sys
import codecs
import re

fileOpen = codecs.open("tweet.txt","r","utf-8")

pattern = re.compile(u"(@)(.+?)(\W)")

for line in fileOpen:
	match = pattern.search(line)
if match:
	print match.group(2)

