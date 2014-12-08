#!/usr/bin/env python
#-*- coding:utf8 -*-

import sys

unigram_count = {}
unigram_total_count = 0
for line in open("medline_sent_tok_stem.txt","r"):
	word = line.strip()
	unigram_total_count += 1
	if word not in unigram_count:
		unigram_count[word] = 1
	else:
		unigram_count[word] += 1
	

bigram_total_count = 0
f = open("medline_bigram_count.txt","r")
for line in f:
        words = line.strip().split()
        bigram_total_count += int(words[0])
print bigram_total_count
f.close()


f = open("medline_bigram_count.txt","r")
for line in f:
        words = line.strip().split()
        Pw = float(unigram_count[words[2]])/unigram_total_count
        Pwz = float(words[0])/bigram_total_count
        P = float(Pwz)/Pw
        print str(P) + "\t" + words[1] +"\t" + words[2]

