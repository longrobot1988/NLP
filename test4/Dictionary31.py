#!/usr/bin/env python
#-*- coding:utf8 -*-

#
#Author:Weilong GUO
#

import sys

f = open("inflection.table.txt","r")

dictionary = {}
for line in f:
	words = line.strip().split("|")
	dictionary[words[0]] = (words[1],words[3],words[6])

	#1.単語（活用）、2.品詞、４.活用形、７.基本形	


#辞書の全てのキーと値をたどる
for i,j in dictionary.items():
	print i,j
