#!/usr/bin/env python
# coding:utf-8
#
#Author:Weilong Guo
#created at:2014-11-13

#read the english test file and splite the ariticle into sentence by

import sys

for line in open(sys.argv[1]):
	for sentence in line.strip().rstrip('.').split('. '):
		print sentence+'.'
#strip() 文字列の先頭およびしりを除去したコピーを返す　rstrip() lstrip()
#split() sepをt単語の境界として文字列を単語に分割し