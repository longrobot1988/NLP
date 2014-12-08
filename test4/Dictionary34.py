#!/usr/bin/env python
#-*- coding:utf8 -*-

import sys
import re
import marshal

f1 = open("dictionary","r")
f2 = open("medline_sent_tok_stem","r")
dic = marshal.load(f1)

for line in f2:
	word = line.strip()
	if word not in dic:
		print word

f1.close()
f2.close()
