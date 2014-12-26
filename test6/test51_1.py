#!/usr/bin/env python
#-*- coding:utf8 -*-
#
#Authour:Weilong Guo
#
#created on: 2014/12/6
#日本語の文書をCabChaで係り受け解析し、ラティス形式(-f1プション)の解析結果を得よ
#係り受け解析とは文節の「修飾する」「修飾される」の関係を調べることです。

#1.*  2.文節番号 3.係り先の文節番号（かがり先なし：−１）4.主辞の形態素番号/機能語の形態番号　5.係り関係のスコア
#1.表層形（Tab区切り）　2.品詞　3.品詞細分類1、4.品詞細分類２、５、品詞細分類３、６、活用形　７、活用型、８原形、読み
#

import CaboCha, sys

def cabochaParse(sentence):
	#
	c = CaboCha.Parser()
	#print c
	tree = c.parse(sentence)
	return tree.toString(CaboCha.FORMAT_LATTICE)


if __name__ == '__main__':
	#for line in sys.stdin.readlines():
	f = open("japanese.txt","r")
	for line in f:
		print cabochaParse(line)
	f.close()
