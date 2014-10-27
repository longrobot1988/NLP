#!/usr/bin/en Python
#-*- coding: utf8 -*-

import sys
import os

file1 = open(sys.argv[1],"r")
col1 = []

for line in file1:
	words = line.split("\t")
	col1.append(words[0])


print len(set(col1))