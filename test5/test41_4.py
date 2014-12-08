#/user/bin/python
#-*-coding:utf-8-*-
#(41) 日本語の文章をMeCabで形態素解析し，その結果を読み込むプログラムを実装せよ．ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，１文は形態素（マッピング型）のリストとして表現せよ．
#python test41.py japanese.txt
import sys,MeCab,pickle
#text=[sentence1,sentence2,.....]
#sentence=[morpheme1,morpheme2,....]
#morpheme={"surface":表層系,"base":基本形,"pos":品詞,"pos1":品詞細分類１}
#text[m][n]["surface"]

import sys
import MeCab

tagger = MeCab.Tagger("")

sent_list=[]
for line in open("japanese.txt","r"):
	line = line.strip()
	node = tagger.parseToNode(line)

	sent_morphs = []
	while node:
		morph_dict = {}
		if node.surface is "":
			pass
		else:
			surface = node.surface
			feature_list = node.feature.split(",")
			morph_dict["surface"] = surface
			morph_dict["base"] = feature_list[6]
			morph_dict["pos"] = feature_list[0]
			morph_dict["pos1"] = feature_list[1]
			sent_morphs.append(morph_dict)
		node = node.next


	sent_list.append(sent_morphs)

for sent in sent_list:
	for morph in sent:
		print morph["surface"],morph["base"],morph["pos"],morph["pos1"]
