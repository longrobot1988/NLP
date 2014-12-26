#!/usr/bin/env python
#-*- coding:utf8 -*-
#
#Authour:Weilong Guo
#
#created on: 2014/12/6
#
#(52)形態数を表すクラスMorphを実装せよ、このクラスは表層形（surface),基本形（base）、品詞（pos）
#品詞細分類1(pos1)をメンバ変数に持つこととする.さらに（51）の解析結果を一文ごとに読み込み、一文をMorphオブジェクトとして
#表現し、適当に表すプログラムを実装せよ。
#cabocha -f japanese.txt >japanese_cabocha.txt

class Morph:
	def __init__(self, surface, base, pos, pos1):
		self.surface = surface
		self.base = base
		self.pos = pos
		self.pos1 = pos1


def test_morph():
	import re
	all_sent_list = []
	one_sent_list = []
	#
	for line in open("japanese_cabocha.txt"):
		if "\t" in line:
			item = re.split(r"\t|,",line.strip());
			one_sent_list.append(Morph(item[0],item[7],item[1],item[2],))
		elif "EOS" in line:
			for item in one_sent_list:
				print 'surface=%s\tbase=%s\tpos=%s\tpos1=%s' % (item.surface, item.base,item.pos,item.pos1)
			all_sent_list.append(one_sent_list)
			print "EOS"
			one_sent_list = []

if __name__ == '__main__':
	test_morph()