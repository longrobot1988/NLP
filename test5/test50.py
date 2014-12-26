#!/usr/bin/env python
#-*- coding:utf8 -*-

#
#Author:Weilong Guo
#
#(48)の出力を利用して、文字列の出現頻度の順位（高い順）を横軸、その出現頻度を縦軸として、プロットせよ
import matplotlib.pyplot as plt
dict={}
listx,listy=[],[]
j=0

for line in open("/Users/kubotanaoyuki/Desktop/NPL/NLP100knock-master/japanese_frequence.txt"):
	w,i = line.strip().split(" ")
	dict[w]=int(i)
	if j < 200:
		listx.append(j)
		listy.append(int(i))
		j+=1

plt.plot(listx,listy)
plt.title('title')
plt.xlabel(' Type ')
plt.ylabel(' Frequency ')
plt.xlim(0,100)
plt.ylim(0,300)
plt.show()	