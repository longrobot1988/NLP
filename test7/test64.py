#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/06/10 15:43:57
#Author:Guo Weilong
"""63の結果を用い、TF*IDF値が高い名詞句トップ100のリストを作成せよ。このとき、数字を含む表現はトップ100のリスト
から除外せよ。	
"""

def sort_tf_idf():
	import re
	dict	=	{}
	for line in open("63_output_tf_idf.txt"):
		word,tf_idf,tf, df 	=	line.strip().split("\t")
		r 	=	re.compile(r"[0-9]")
		if not r.search(word):
			dict[word]		=	float(tf_idf)
	return dict

def print_tf_idf(dict):
		j	=	0
		for word,i in	sorted(dict.items(),key	= lambda x:x[1],reverse	= True):
			if j>=100:
				break
			print word ,i
			j+=1

if __name__ == '__main__':
	dict	=	sort_tf_idf()
	print_tf_idf(dict)