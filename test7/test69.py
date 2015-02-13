#!/usr/bin/python
#-*-coding:utf-8-*-
#Author:Guo Weilong

"""(69) 68の結果を名詞句をノードとする無向グラフとみなし，Graphvizを使ってグラフを描画せよ．すなわち，68の出力をGraphvizの入力フォーマットであるDOT形式に変換するプログラムを実装すればよい．グラフを描画するときは「neato -Tsvg」コマンドを用い，SVG形式に書き出すとよい．"""
def test69():
	print "graph knock69{"
	for line in open("68_output.txt"):
		item = line.strip().split('\t')
		print '\t"%s" -- "%s"[label="%s"];' % (item[1],item[2],item[0][0:5])
	print "}"

if __name__ == '__main__':
	test69()