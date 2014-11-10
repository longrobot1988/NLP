#!/usr/bin/env python
#_*_coding:utf-8 _*__
#
#Author:Weilong Guo
#人の名前を抽出せよ		

import sys
import codecs
import re

fileOpen = codecs.open("tweet.txt","r","utf-8")

pattern = re.compile(ur"((?<!みな)|(?<!皆))(さん|氏|ちゃん|くん|先生)")


for line in fileOpen:
   match = pattern.search(line)
   if match:
      print line.strip()
