#!/usr/bin/python
#-*-coding:utf-8-*-
"""(10) 各行の２コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べよ．ただし，(3)で作成したプログラムの出力（col2.txt）を読み込むプログラムとして実装せよ．確認にはcut, uniq, sortコマンドを用いよ．"""



import sys

file = open("col2.txt", "r")
dict = {}
for line in file:
	if line in dict:
		dict[line] += 1
	else:
		dict[line] = 1
		sorted_list = sorted(dict.items(), key=lambda x: x[1], reverse=True)
		for val in sorted_list:
				print str(val[1]) + " " + val[0].strip()