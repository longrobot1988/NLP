#!/usr/bin/env python
#-*- coding:utf8 -*-
#
#:Author Weilong Guo

import sys
import re
import marshal

f1 = open("dictionary_1.txt","r")
f2 = open("medline_sent_tok_stem","r")
dic = marshal.load(f1)

#marshal モジュールはpython値をバイナリ形式で読み書きできるような関数が含まれている		

for line in f2:
	word = line.strip()
	if word in dic:
		print word,dic[word]

f1.close()
f2.close()
