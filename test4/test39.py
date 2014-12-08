#!/usr/bin/env python
#-*- coding:utf8 -*-

#
#Author:Weilong Guo
#
#(39) (38)の出力を読み込み、ある単語wに続く単語zの条件付き確率P(z|w)を値とする
#ハッッシュデータベースを構築せよ、ハッシュデータベースの構築には、Kyoto CabinetのPythonモジュールを用いよ
#ただし、Kyoto CabinetのPythonモジュールはすでに導入済みであるので、各自でインストール作業をおこなわなくてもよい

import sys
from kyotocabinet import *

db = DB()
db.open("sample.kch")

for line in sys.stdin:
	line = line.strip()
	(prob,pre,post) = line.split("\t")
	db.set((pre,post),prob)		