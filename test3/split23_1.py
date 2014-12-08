#!/usr/bin/env python
#-*-coding:utf-8-*-
#
#Author:Weilong Guo
#英語テキストを行に区切る	

import sys

for line in open('medline.txt'):
	itemList = line.strip().split(' ')
	for w in itemList:
		w = w.replace('.','\n')
		print w