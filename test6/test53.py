#!/usr/bin/env python
#-*- coding:utf8 -*-
#
#Authour:Weilong Guo
#
#created on: 2014/12/6
#
#(53)文節を表すクラスCHunkを実装せよ.このクラスは形態素のリスト（morphs）、係り先文節インデックス番号（dst）
#係り先文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする。さらに、（５１）の解析結果を１文毎に読み込み、
#１分をChunkオブジェクトのリストとして表現し、適当に表示するプログラムを実装せよ。	

from collections import defaultdict
import re

class Morph:
	def __init__(self,surface,base,pos,pos1):
		self.surface	=	surface
		self.base		=	base
		self.pos 		=	pos
		self.pos1		=	pos1

class Chunk:
	def __init__(self,num,morphs,dst,srcs):
		self.num		=	num
		self.morphs		=	morphs
		self.dst		=	dst
		self.srcs		=	srcs




def test_Morph():
	one_sent	=	[]
	all_sent	=	[]
	#新しいディクショナリ状のオブジェクトを返す　defaultdict(default_factory[])
	#listをdefaultdictとすることで、キー＝値ペアのシーケンスリストの辞書へ簡単にグループ化できます。
	#順番		
	kakari_dict	=	defaultdict(list)
	for line in open("japanese_cabocha.txt"):
		if '* ' in line:
			w			=	re.split(r" ",line.strip())
			w[2]		=	w[2][:0]
			one_chunck	=	Chunk(w[1],[],w[2],[])
			kakari_dict[w[2]].append(w[1])
			one_sent.append(one_chunck)
		elif "\t" in line:
			item		=	re.split(r"\t|,",line.strip())
			one_chunck.morphs.append(Morph(item[0],item[7],item[1],item[2]))
		elif "EOS"	in line:
			for one_chunck in one_sent:
				one_chunck.srcs	=	kakari_dict[one_chunck.num]
				for morphs in one_chunck.morphs:
						print 'surface=%s\tbase=%s\tpos=%s' % (morphs.surface,morphs.base,morphs.pos)
				print 'num=%s\tdst=%s\tsrcs=%s' 		% (one_chunck.num,one_chunck.dst,one_chunck.srcs)
				all_sent.append(one_sent)
				print "EOS"	
				one_sent		=	[]
				kakari_dict		=	defaultdict(list)



if __name__ == '__main__':
	test_Morph()

if __name__ == '__main__':
		test_Morph()	