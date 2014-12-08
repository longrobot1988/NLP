#!/usr/bin/env python
#-*-coding:utf-8-*-
#
#Author:Weilong Guo
#
	

import sys

for line in open('medline_1.txt'):
	itemList = line.strip().lower()

	print (line.strip() +"\t"+itemList)