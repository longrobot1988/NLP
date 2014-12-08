#!/usr/bin/env python
#-*-coding:utf-8-*-
#
#Author:Weilong Guo

import sys
from collections import Counter

def test10_1(list1):
	counter = Counter(list1)
	for word, cnt in sorted(counter.most_common(), key=lambda x:x[1], reverse = True):
		print word, cnt

if __name__ == '__main__':
	list1=[]
	for line in open("medline_1.txt", "r"):
		list1.append(line.strip())
		test10_1(list1)