#!/usr/bin/env python
#-*-coding:utf-8-*-
#
#Author:Weilong Guo
#英語テキストを行に区切る			


import sys
import re

import sys
sys.path.append(r"/Users/kubotanaoyuki/Desktop/NPL/practise/NLP/test3")

from split import split

f = open("medline_sent.txt","r")
print("input your charactor.")
print(" please input \"\w\"":)
s = raw_input("raw_input:")


words = []
for line in f:?
    sent = split(line,s)
    words += sent

for w in words:
    if w.endswith(","):
        w = w[:-2]
    elif w.endswith("."):
        w =w[:-2]+"\n"
    print w

