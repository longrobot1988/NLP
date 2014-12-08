#!/usr/bin/env python
#-*- coding:utf8 -*-
#
#Authour:Weilong Guo
#
#created on: 2014/12/6
#(41)日本語の文書をMeCabで形態素解析し、その結果を読み込むプログラムを実装せよ.ただし、各形態は表層形(surface)
#基本形（Base）、品詞（pos）,品詞細分類１（pos1）	をキーとするマッピング型に格納し、一文は形態素(マッピング型)
#のリストとして表現せよ。

import MeCab
doc =[]
mc = MeCab.Tagger("mecabrc")
#表層形\t品詞、品詞再分類1,品詞再分類2、品詞再分類3,活用形、原型、読み、発音

for line in open("japanese.txt"):
	one_sent=[]
	line = mc.parse(line.strip())
	print line
	itemlist = line.strip().split("\n");
	for item in itemlist:
		if item == "EOS" or item =="":
			break
			surface,item2 = item.strip().split("\t")
			item3 = item2.split(",")
			dict = {"surface":surface,"base":item3[6],"pos":item3[0],"pos1":item3[1]}
			one_sent.append(dict)
		doc.append(one_sent)
	print doc


