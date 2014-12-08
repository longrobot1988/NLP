#!/usr/bin/env python
# coding:utf-8
#
#Author:Weilong Guo
#created at:2014-11-13

#read the english test and seperate the article into sentence by period and space and uppercase 
#secondly seperate the sentence into word

import sys
import re

def convertTestIntoLine(line):
	sentenceBoundary = re.compiler(r'\.([A-Z])')
	#re.compiler正規表現	
	#特殊文字をエスケープする
	#[a-z] [A-Z]
	#[0-9A-Fa-f]:全ての十六進数
	line = line.strip()
	return re.sub(r'\.([A-Z])',r'.\n\1',line)
	#string内で、重複しないpatternのマッチをreplで置き換えた文字列を返す
	#(ドット）デフォルトのモードでは改行以外の任意の文字にマッチする。

if __name__ == '__main__':
	for line in open(sys.argv[1]):
		print convertTestIntoLine(line.strip())
