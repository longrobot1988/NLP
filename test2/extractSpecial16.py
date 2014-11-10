#!/usr/bin/env python
#_*_coding:utf-8 _*__
#
#Author:Weilong Guo
#指定される部分を交換する		

import sys
import codecs
import re

fileOpen = codecs.open("tweet.txt","r","utf-8")

pattern = re.compile(ur"[\u4e00-\u9fff]\([A-Z]+\)")
#文字の集合を指定する
#/u4e00-\u9fff  漢字
#[A-Z] 
#\ 特殊文字をエスケープする

for line in fileOpen:
   match = pattern.search(line)
   if match:
      print line.strip()
