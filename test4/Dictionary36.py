#!/usr/bin/env python
#-*- coding:utf8 -*-

#
#Authour:Weilong Guo
#


import sys

words = []
for line in open("medline_sent_tok_stem.txt","r"):
	word = line.strip()
	words.append(word)

output = open("medline_bigram.txt","w")
for i in range(0,len(words)-1):
	print words[i] + "\t" +words[i+1]
	output.write(words[i] + "\t" +words[i+1] + "\n")

output.close()
