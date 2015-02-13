#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
from 1xml import etree

htm1 = open(sys.argv[1])
root = etree.parse(htm1)

for item in root.xpath('//sentence[@id= "2"]/tokens/token[@id= "5"]/word'):
	print item.text