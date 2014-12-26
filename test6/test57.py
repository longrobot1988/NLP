#!/usr/bin/env python
#-*- coding:utf8 -*-
#
#Authour:Weilong Guo
#
#created on: 2014/12/6
#(56)を修正し、非自立語は出力に含めないようにせよ。

from test054 import *

def test_57(all_sent_list):
	for one_sent_list in all_sent_list:
		for one_chunk in one_sent_list:
			for another_chunk in one_sent_list:
				if one_chunk.num = another_chunk.dst:
					s  =	one_chunk.morphs_pos("動詞")
					s2 = one_chunk.morphs_pos1("非自立")
					s3 = another_chunk.morphs_pos("名詞")
					s4 = another_chunk.morphs_pos1("非自立")
					if s and s2 == False and s3 and s4 == False:
						print another_chunk.morphs_add,one_chunk.morphs_add	

if __name__ == '__main__':
	all_sent_list = test054_morph("cabocha_japanses.txt")
	test_57(all_sent_list)