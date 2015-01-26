#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/06/10 15:43:57
#Author:Guo Weilong

"""(57)の出力を「係り元」->「係り先」の有向グラフとみなし、Graphvizを使ってグラフを描画せよ。
すなわち、（５７）の出力をGraphvizの入力フォーマットであるDOT形式に変換するプログラムを実装すればよい.
グラフを描画するときは「neato-Tsvg」コマンドを用い、SVG形式に書き出すとよい	
"""

def test060():
	print "digraph knock60{"
	for line in open("test057.txt"):
		item	=	line.replace('\"',r'\"')
		item	=	item.strip().split('\t')
		print  '\t"%s" -> "%s";' % (item[0],item[1])
	print "}"


if __name__ == '__main__':
	test060()