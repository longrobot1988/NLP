#!/usr/bin/env python
#-*- coding:utf8 -*-
#
#Authour:Weilong Guo
#
#created on: 2014/02/09
#

#1番目の文の5番目のlemmaを並べたもの	

import sys
from lxml import etree

html = open(sys.argv[1])
root = etree.parse(html)
for item in root.xpath('//sentence[@id= "1"]/tokens/token/lemma'):
	print item.text
