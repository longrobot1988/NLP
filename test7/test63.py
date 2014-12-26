#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/06/10 15:43:57
#Author:Guo Weilong
"""(62)の結果を用い、それぞれの名詞句のTF*IDF値を計算し、"(名詞句)\t(TF値)\t(DF値)"の形式で出力せよ。
ある名詞句wがあるとき、freq(w)をコーパス全体での名詞句Wの出現頻度,df(w)を名詞wが出現するファイルの数、
Nを総ファイル数とし、TF*IDF値はfreq(w)*log(N/df(w))として計算せよ。	
"""

#TFはTerm Frequencydでそれぞれの単語の文書内での出現頻度を表す。
#IDFはInverse Document Frequencydでそれぞれの単語のが
# tf(t,d)(文書d内のある単語tのTF値）	= ある単語tの文書d内での出現回数/文書d内の全ての単語の出現回数の和
#　idf(t)(ある単語tのiDF値)=log(N/df(t))+1  N:全文書数　df(t) ある単語tが出現する文書の数

import re,glob,sys,math
from collections import defaultdict

def make_dict():
	set_list	=	[]
	#新しいディクテーション状のオブジェクトを返す。
	#lambda <arg1>,<arg2>,<arg3>,<arg4>,<argN>:expressions
	all_dict	=	defaultdict(lambda:0)
	#全てのファイル数を計算する
	N 			=	len(glob.glob('62_output_japanese_?.txt'))
	for name in glob.glob('62_output_japanese_?.txt'):
		#set([]):iterableから要素と取り込んだ、新しいsetもしくはfrozensetオブジェクトを返す
		#iterableが指定されないならば、新しい空のsetが返されます
		word_set=	set([])
		for line in open(name):
			ward_set.add(line.strip())
			all_dict[line.strip()]	+=	1
			set_list.append(ward_set)
		return all_dict,set_list,N

def make_tf_idf():
	for word ,ii in sorted(all_dict.items(),key=lambda x:x[1],reverse = True):
		i = 0
		for ward_set in set_list:
			if word in ward_set:
				i+=1
		print '%s\%.6f\t%d\t%d' % (word,(all_dict[word]*math.log(float(N)/i,2)),all_dict[word],i)

if __name__ == '__main__':
	all_dict,set_list,N = make_dict()
	make_tf_idf(all_dict,set_list,N)