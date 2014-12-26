#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/12/22

"""(54) 以降のプログラムを実装しやすくするため，
(53)のプログラムをモジュール化せよ．"""


#高性能なコンテナ・データ型
#あたらしディクショナリ状のオブジェクトを返す
#正規表現マッチング操作を提供しています。
from collections import defaultdict
import re


#
class Morph:
	def __init__(self, surface, base, pos, pos1):
		self.surface = surface
		self.base = base
		self.pos = pos
		self.pos1 = pos1



class Chunk:
	def __init__(self, num, morphs, morphs_add, dst, srcs,main_word,main_pos):
		self.num = num
		self.morphs = morphs
		self.morphs_add = morphs_add
		self.dst = dst
		self.srcs = srcs
		self.main_word = main_word
		self.main_pos = main_pos

	def morphs_pos(self,w):
		for morphs in self.morphs:
			if morphs.pos == w:
				return True
		return False

	def morphs_pos1(self,w):
		for morphs in self.morphs:
			if morphs.pos1 == w:
				return True
		return False

def morphs_not_kigo(self):
	w = ""
	for morphs in self.morphs:
		if morphs.pos != "記号":
			w = w + morphs.surface
		return w

def morphs_base_return(self):
	for morphs in self.morphs:
		if morphs.pos == "名詞" or morphs.pos == "動詞" or morphs.pos == "形容詞":
			if morphs.base != "*":
				return morphs.base
			else:
				return morphs.surface
	return False


def test054_morph(open_file):
	#list をdefault_factoryとすることで、キー＝値ペアのシーケンスをリストの辞書へ簡単にグループ化できます。
	kakari_dict = defaultdict(list)
	#二つのリストを生成する
	#一行の内容のリスト
	#EOSをエンドで終了の内容
　　　
	one_sent = []
	all_sent_list = []

	for line in open(open_file):
		#カボチャで分析結果によって　
		if "* " in line:
			w = re.split(r" |/", line.strip())
			#係り先の文節番号を抽出する	

			w[2] = w[2][:-1]
			one_chunk = Chunk(w[1], [], "", w[2], [], "", "")
			#w[1]をw[2]の右側に付け加える。
			kakari_dict[w[2]].append(w[1])
			#オブジェクトをone_sentのリストに追加する。	
			one_sent.append(one_chunk)
			i = 0
		elif "\t" in line:
			#カボチャで分析結果によって
			#両側はスベスを除くstring　"\t"あるいは","を分割する
			item = re.split(r"\t|,", line.strip())
			#クラスMorphの初期化、かつ表層形　基本形　品詞 品詞1
			one_chunk.morphs.append(Morph(item[0], item[7], item[1], item[2]))
			#もし、品詞は記号と等しくない。
			if item[1] != "記号":
				#品詞を追加する
				one_chunk.morphs_add = one_chunk.morphs_add + item[0]
				#主辞の形態素番号/機能語の形態素番号	
				if i == int(w[3]):
					if item[7]== "*":
						item[7] = item[0]
					one_chunk.main_word = item[7]
					one_chunk.main_pos = item[1]
			i+=1
		elif "EOS" in line:
			for one_chunk in one_sent:
				one_chunk.srcs = kakari_dict[one_chunk.num]
			all_sent_list.append(one_sent)
			one_sent = []
			kakari_dict = defaultdict(list)
	return all_sent_list

if __name__ == '__main__':
	all_sent_list = test054_morph("japanese_cabocha.txt")





