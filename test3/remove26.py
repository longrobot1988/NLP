#!/usr/bin/env python
#-*-coding:utf-8-*-
#
#Author:Weilong Guo
	

import re

for line in open('medline_1.txt'):
	m = re.match(r'.+ness|.+ly',line.strip())
	#'.' 改行以外の任意の文字にマッチする
	#
	if m :
		print line.strip()