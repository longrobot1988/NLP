#!/usr/bin/env python
#-*- coding:utf8 -*-
#
#Authour:Weilong Guo
#
#created on: 2014/12/6
#文書中の[AのB]という表現(AとBは名詞の1形態素)

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
	for morph in sent[:-2]:
		if morph["pos"] == "名詞":
			l = sent.index(morph)
			if sent[l+1]["surface"] == "の"and sent[l+2]["pos"]== "名詞":
				print morph["surface"] + sent[l+1]["surface"]\
				+sent[l+2]["surface"]

