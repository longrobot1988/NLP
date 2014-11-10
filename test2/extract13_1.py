#!/usr/bin/env python
#_*_coding:utf_8 _*_
#
#Author:Weilong Guo
#非公式RTのスイートの中で、RT先へのコメント部分のみを抽出せよ

import sys 
import re	#正規表現のモジュール
import codecs #標準で日本語を扱うモジュール

fileOpen = codecs.open("tweet.txt","r","utf-8")

pattern = re.compile(u"^.+ : (.*[^RT].*) RT+?")
#

for line in fileOpen:
 match = pattern.search(line)
 if match:
 	print match.group(1).strip()			



