#!/usr/bin/env python
#-*-coding:utf-8-*-
#
#Author:Weilong Guo
#英語テキストを行に区切る			


import sys
import re

f = open("medline.txt","r")

sent = []

for line in f:
    m = 0
    n = 1
    for w in line:
        n += 1
        if w == ".":
            print(line[m:n])
            sent.append(line[m:n])
            m = n


output = open("medline_sent.txt","w")
for s in sent:
    output.write(s+"\n")

f.close
output.close