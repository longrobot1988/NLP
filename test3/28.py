#!/usr/bin/env python
#-*- coding:utf8 -*-

import sys
sys.path.append(r"/Users/tora/Documents/NLP 100/03 ")
from test10 import tops

f = open("medline_sent_tok.txt","r")

bigram = []
for line in f:

    n = 0
    for w in line[:len(line)-1]:
        bigram.append(line[n]+line[n+1])
        n +=1
        


output = open("bigram.txt","w")
for w in bigram:
    output(w)

top = tops(w)
for item,value in top[:99]:
    print item,value


