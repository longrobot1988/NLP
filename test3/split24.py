#!/usr/bin/env python
#-*-coding:utf-8-*-
#
#Author:Weilong Guo
#各トークン最後が記号で終わる場合は、その記号を別のトークンとして分離せよ			

import re


r = re.compile(r'( |\.$|\,$|\. |\, )')


for line in open('medline.txt'):
	itemList = r.split(line.strip())

	while ' ' in itemList:
		itemList.remove(' ')
		
		for w in itemList:
			print w
