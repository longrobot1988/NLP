#!/usr/bin/env python
#-*- coding:utf8 -*-
#
#Authour:Weilong Guo
#
#created on: 2014/02/09
#

#1番目の文の4番目のトークンの、係り受け構造上での子(dependent)の単語Wikipediaのタンプ（XML形式）を解析し、
#以下の情報を抽出せよ.ただし、XML形式の解析にはXML.SAXモジュールを用いよ

import sys
from lxml import etree

html = open(sys.argv[1])
root = etree.parse(html)

for item in root.xpath('//sentence[@id= "1"]/dependencies[@type= "basic-dependencies"]/dep/governor[@idx= "4"]'):
	for d in item.getparent().iter('dependent'):
	print d.text	
