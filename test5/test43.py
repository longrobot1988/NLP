#!/usr/bin/env python
#-*- coding:utf8 -*-
#
#Authour:Weilong Guo
#
#created on: 2014/12/6
#文書中に出現する全ての動詞の基本形を抜き出せ
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
		if morph["pos"] == "動詞":
			print morph["base"]