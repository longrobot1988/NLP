#!/usr/bin/env python
#-*- coding:utf8 -*-
#
#Authour:Weilong Guo
#
#created on: 2014/12/6
#名詞を含む文節が、動詞を含む文節に係るとき、これらをタブ句切り形式で抽出せよ。

from test54 import *

def test_56(all_sent_list):
	for one_sent_list in all_sent_list:
		for one_chunk in one_sent_list:
			for another_chunk in one_sent_list:
				if one_chunk.num		==	another_chunk.dst:
					s 	=	one_chunk.morphs_pos("動詞")
					s2	=	another_chunk.morphs_pos("名詞")
					if s and s2:
						print "%s\t%s" %(another_chunk.morphs_add,one_chunk.morphs_add)

if __name__ == '__main__':
	all_sent_list	=	test054_morph("japanese_cabocha.txt")
	test_56(all_sent_list)


