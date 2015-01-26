#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/06/10 15:43:57
#Author:Guo Weilong
"""
(75)74で作成したプログラムを改変し、以下の11種類の素性を抽出・表示するプログラムを実装せよ。
ただし、これらの素性はタブ区切り形式で”＃（名詞句）\n(冠詞タイプ)\t（タブ区切り形式の素性）\n”という形式で出力せよ・
例えば、”A major challenge is [the limited number] of NOE restraints ........”の[]の部分の名詞句に対して、
次の出力を得る（ただし”\”は実際にはここで改行しないことを表す）	
○ hw 		=	(末尾)
○ hpos　		=	(末尾の品詞)
○ hw|hpos 	=	(末尾の品詞)|（末尾の品詞）
○ fw 		=	(先頭の単語)
○ fpos		=	(先頭の品詞)
○ fw|fpos	=	(先頭の品詞)| (先頭の単語)
○ w[0]		=	(名詞句の単語列)
○ w[-1]		=	(名詞の１語前の単語)
○ pos[-1]	=	(名詞句の１語前の品詞)
○ w[1]		=	(名詞句の１語後の単語）
○　pos[1]	=	(名詞句の１語後の品詞)
"""

from test072 import *

class feature:
	def __init__(self,pre_w,pre_pos,head_w,f_pos):
		self.pre_w		=	pre_w
		self.pre_pos	=	pre_pos
		self.head_w		=	head_w
		self.f_pos		=	f_pos

def find_head(w):
	if w == 'a' or w =='an' or w =='the':
		return w.upper()
	else:
		return "NONE"

def make_feature(w,feature,next_w,next_pos,hpos):
		item			=	w.split()
		if feature.head_w != "NONE" and len(item)>2:
			i=2
		else:
			i=1
		w_0				=' '.join(item[i:])
		fw				=	item[i]
		fpos 			=	feature.f_pos
		hw 				=	item[-1]


def test75(all_sent_list):
	for one_sent_list in all_sent_list:
		w 		= 	''
		pre_w	= 	"None"
		pre_pos	=	"None"
		for one_chunk in one_sent_list:
			if one_sent_list.chunk == "B-NP":
				if w.startswith('#'):
					make_feature(pre_w,pre_pos,head_w,one_chunk.pos)
				head_w		=	find_head(one_chunk.surface.lower())
				featrues	=	feature(pre_w,pre_pos,head_w,one_chunk.pos)
				w 			=	'#' + one_chunk.surface
		 	elif one_chunk.chunk == "I-NP" and w !=' ':
		 		if featrues.head_w != "NONE":
		 			featrues.f_pos	=	one_chunk.pos
		 		w 			=	w + ' ' + one_chunk.surface
		 	elif w !=' ':
		 		make_feature(w,featrues,one_chunk.surface,one_chunk.pos,pre_pos)
		 		w 			=	''
		 	else:pass
		 	pre_w	=	one_chunk.surface
		 	pre_pos =	one_chunk.pos

if __name__ == '__main__':
	all_sent_list	=	test72('71_GENIA_tagger_1.txt')
	test75(all_sent_list)