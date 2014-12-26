#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/06/10 15:43:57 Shin Kanouchi
"""58 係り元が二つ以上ある文節に対し、その文節とすべての係り元を表示せよ。		
"""

from test054 import *

def test_58(all_sent_list):
	for one_sent_list in all_sent_list:
		for one_chunk in one_sent_list:
			if len(one_chunk.srcs) > 1:
				for another_chunk in one_sent_list:
					if one_chunk.num == another_chunk.dst:
						print '%s\t%s' %(another_chunk.morphs_add, one_chunk.morphs_add)



if __name__ == '__main__':
	all_sent_list = test54_morph("japanese_cabocha.txt")
	test_58(all_sent_list)

