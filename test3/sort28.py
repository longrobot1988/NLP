#!/usr/bin/python
#-*-coding:utf-8-*-

#
#Authour:Weilong Guo
#

import sys
from collections import Counter

def test10_1(list):
	counter = Counter(list)
	for word, cnt in sorted(counter.most_common(), key=lambda x:x[1], reverse = True):
		print word, cnt

if __name__ == '__main__':
	i = None
	list=[]
	for line in open('medline_1.txt'):
		line = line.strip()
		if i is not None:
			list.append(i+' '+line)
		i= line
		
	test10_1(list)