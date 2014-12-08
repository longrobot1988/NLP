#!/usr/bin/env python
#-*- coding:utf8 -*-
#
#Authour:Weilong Guo
#
#created on: 2014/12/6
#日本語の文書をCabChaで係り受け解析し、ラティス形式(-f1プション)の解析結果を得よ
#係り受け解析とは文節の「修飾する」「修飾される」の関係を調べることです。

import CaboCha
def cabocha_japanese():
	N = CaboCha.Parser()
	for line in open("japanese.txt"):
		m = N.parseTostring(line)
		print m


if __name__ == '__main__':
	cabocha_japanese()


