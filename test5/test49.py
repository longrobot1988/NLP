#!/usr/bin/env python
#-*- coding:utf8 -*-

#
#Author:Weilong Guo
#
#(48)の出力を利用して、文字列の頻度を横軸、その文字列の異なり数（種類数）を縦軸として、ヒストグラムをプロッオせよ、
#なお、プロットにはgnuplotやmatplotlibを用い、グラフを画像ファイルとして保存せよ.


import matplotlib.pyplot as plt
dict={}

for line in open("/Users/kubotanaoyuki/Desktop/NPL/NLP100knock-master/japanese_frequence.txt"):
	w,i = line.strip().split()
	dict[w] = int(i)

#プロット領域
fig = plt.figure()
ax = fig.add_subplot(111)
ax.hist(dict.values(), bins=len(dict.values()), range=(0, 150))
plt.title('title')
plt.ylabel('type(kotonari)')
plt.xlabel('Frequency')
ax.set_xlim(0,150)
ax.set_ylim(0,100)
plt.savefig("plt_retest49.eps")
plt.show()