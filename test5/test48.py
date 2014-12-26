#!/usr/bin/env python
#-*- coding:utf8 -*-

#
#Author:Weilong Guo
#
#標準入力から読み込んだ各行の文字列の頻度をまとめるプログラムを書き、（４７）のプログラムと組み合わせることによって、
#文書中に出現する各動詞	の出現頻度を求めよ、さらに出現頻度の高い順に動詞を並べよ。

import re
from collections import Counter
v_list=[]
i = 0

#line = 表層\品詞細分類１、品詞再分類２、品詞再分類３、活用形、活用形、原型、読み、発音
for line in open("japanese_mecab.txt"):
	if line.strip() !="EOS":
		item = re.split(r"\t|",line.strip())
	if item[1] == "動詞":
		v_list.append(item[7])
#リストに現れる単語と単語数
counter = Counter(v_list)

for word,cn in sorted(counter.most_common(),key=lambda x:x[1],reverse = True):
	print word,cnt
