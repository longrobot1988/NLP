#!/user/bin/python
#-*-coding:utf-8-*-
#(41) 日本語の文章をMeCabで形態素解析し，その結果を読み込むプログラムを実装せよ．ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，１文は形態素（マッピング型）のリストとして表現せよ．
#python test41.py japanese.txt
import sys,MeCab,pickle
#text=[sentence1,sentence2,.....]
#sentence=[morpheme1,morpheme2,....]
#morpheme={"surface":表層系,"base":基本形,"pos":品詞,"pos1":品詞細分類１}
#text[m][n]["surface"]

import sys
import re

def mecab(FILE):
	result = []
	for line in open(FILE):
		line = line.strip()
		if line !="EOS":
			mecab_list = re.split(r'\t|,',line);
			dict = {'surface':mecab_list[0],'base':mecab_list[6],'pos':mecab_list[1],'pos1':mecab_list[2]}
			result.append(dict)

	print result



if __name__ == '__main__':
	mecab(sys.argv[1])