#!/usr/bin/en python
#coding:utf-8

#
# Author:Weilong Guo
#

import sys
#def paste(filePath1,filePath2):
#	totalLines = sum([ 1 for line in open(filePath1)])
#	file1,file2 = open(filePath1),open(filePath2)
#	for i in range(totalLines):
#		print '%s\t%s' % (file1.readline().strip(),file2.readline())

#	if __name__ == '__main__':
#		paste(sys.argv[1],sys.argv[2])

	if __name__ == '__main__':
		f1,f2 = open('col1.txt','r'),open('col2.txt','r')
		for i in range(len(sys.stdin.readlines())):
			line = f1.readline().rstrip('\n)+'\t'+fe.readline().rstrip('\n')
			print line
			f1.close();
			f2.close();

