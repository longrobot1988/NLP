#!/usr/bin/python
#coding:utf-8
#
# Author:Weilong Guo
#

import sys

def extractKeywords(filePath):
	for line in open(filePath):
		line = line.decode('utf-8')
		if u'拡散希望'in line:
			#sys.stdout.write(line.encode('utf-8'))
			print line.strip()

			if __name__ == '__main__':
				extractKeywords(sys.argv[1])
