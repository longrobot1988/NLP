#!/usr/bin/env python
#-*- coding:utf8 -*-
#
#Authour:Weilong Guo
#
#created on: 2014/12/6
#文書中のすべての名詞の連続(１形態数以上)を抜き出せ

import re
list_N = []

for line in open("japanese_tail10_MeCab.txt"):
	if line.strip() != "EOS":
		item = re.split(r"\t|,",line.strip())
		if item[1] == "名詞":
			list_N.append(item[0])
		elif len(list_N)>1:
			for N in list_N:
				print N
			print ""
			list_N=[]
		else:
			list_N=[]