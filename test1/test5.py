#!/usr/bin/en python
#_*_coding:utf-8 -*-
#
# Author Weilong Guo
#

import sys

def headN(filePath,N):
	file = open(filePath)
	for i in range(N):
		sys.stdout.write(file.readline())

if __name__ == '__main__':
	headN(sys.argv[1],int(sys.argv[2]))