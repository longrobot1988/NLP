#!/usr/bin/env python
#-*- coding:utf8 -*-
#
#Authour:Weilong Guo
#
#created on: 2014/12/6
#(41)日本語の文書をMeCabで形態素解析し、その結果を読み込むプログラムを実装せよ.ただし、各形態は表層形(surface)
#基本形（Base）、品詞（pos）,品詞細分類１（pos1）	をキーとするマッピング型に格納し、一文は形態素(マッピング型)
#のリストとして表現せよ。

import sys
import MeCab
import  pickle

#text = [sentence1,sentence2,.........]
#morpheme = {"surface":表層系、"base":基本形、””	}

def mecab_input(data):
	text=[]
	for line in open(data):
		tagger = MeCab.Tagger("mecabrc")
		sent = tagger.parse(line).strip()
		words = sent.split("\n")
		sentence = []
		for word in words:
			if not word == "EOS":
				word_items = word.split("\t")
				word_items2 = word_items[1].split(",")
				morpheme = {"surface":word_items[0],"base":word_items2[6],"pos":word_items2[0],"pos1":word_items2[1]}
			else:
				pass
		text.append(sentence)
	return text

def main():
	data_japanese = sys.argv[1]
	text = mecab_input(data_japanese)
	output_file = open("test41_output.pickle","w")
	pickle.dump(text,output_file)
	for sent in text:
		for word in sent:
				print "{surface:%s,base:%s,pos1:%s}" %(word["surface"],word["base"],word["pos"],word["pos1"])

if __name__ == '__main__':
	main()
