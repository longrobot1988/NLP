#!/usr/bin/en python
#_*_coding:utf-8 _*_
#
# Author:Weilong Guo


import sys

f = open(sys.argv[1],"r")

#stripは文字列左右から指定文字を削除するメソッド
for line in f:
	l = line.replace("\t"," ").strip()
	print l


