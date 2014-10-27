#!/usr/bin/python
#_*_coding:utf-8 _*_
#
# Author Weilong Guo
#
import sys

n = int (sys.argv[1])
f = open("address.txt","r")
itemList = []


for line in f:
	itemList.append(line)

for k in range(n):
	print itemList[len(itemList)-n+k].strip()