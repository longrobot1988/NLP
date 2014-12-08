#!/usr/bin/env python
#-*- coding:utf8 -*-
#
#Authour:Weilong Guo
#
#created on: 2014/12/6
#(42)から（46）までの処理を一つのプログラムに統合し、処理内容をコマンドライン引数でon/offできるようにせよ、
#コマンドライン引数の処理には、optparseモジュールを用い、オプションには適当な名前(42)は--verb等)とドキュメント
#ドキュメント(-hを引数することで表示される)を書け

import sys
import marshal
#Python値をバイナリ形式で読み書きできるような関数が含まれる
from optparse import OptionParser

parser = OptionParser(usage = u"%prog [-v] [--v2] [--sn] [--ab] [--nn] dumpfile")
#parserモジュールはPythonの内部バーサとバイトコード・コンパイラへのインターフェイスを提供する

parser.add_option('-v','--v1',action='store_true',help=u"全ての動詞を抜き出す")
parser.add_option('--v2',action='store_true',help=u"全ての動詞の原型を抜き出す")
parser.add_option('--sn',action='store_true',help=u"全てのサ変名詞を抜き出す")
parser.add_option('--ab',action='store_true',help=u"全て「AのB」を抜き出す")
parser.add_option('--nn',action='store_true',help=u"全ての名詞の連続を抜き出す")
parser.set_defaults(
	v1 =False,
	v2 = False,
	sn = False,
	ab = False,
	nn = False,
	)
options,args = parser.parse_args()
if len(args)>0:
	text = marshal.load(open(args[0]))

	if options.v1:
		#print　"全ての動詞を抜き出す"
		for sent in text:
			for morph in sent:
				if morph["pos"] == "動詞":
					print morph["surface"]

	if options.v2:
		#print　"全ての動詞を抜き出す"
		for sent in text:
			for morph in sent:
				if morph["pos"] == "動詞":
					print morph["surface"],morph["base"]


	
	if options.sn:
		#print　"全てのサ変名詞を抜き出す"
		for sent in text:
			for morph in sent:
				if morph["pos"] == "動詞" and morph["pos1"]=="サ変接続":
					print morph["surface"]

	if options.ab:
		#print　"全ての「AのB」という表現を抜き出す"
		for sent in text:
			pre_morph = {"surface","pos","pos1"}
			prepre_morph = {"pos":""}
			for morph in sent:
				if prepre_morph["pos"] == "名詞" and morph["pos"]=="名詞"\
					and pre_morph["surface"]=="の" and pre_morph["pos"] =="助詞" and pre_morph["pos1"]=="連体化":
					print prepre_morph["surface"]+""+pre_morph["surface"]+""+morph["surface"]
				prepre_morph = pre_morph
				pre_morph = morph

	if options.nn:
		for sent in text:
			pre_morph = {"pos":""}
			mylist=[]
			pre_id = 0
			for morph in sent:
				if pre_morph["pos"]=="名詞" and morph["pos"]=="名詞":
					if pre_id == id(pre_morph):
						mylist.append(morph["surface"])
					else:
						print " ".join(mylist)
						mylist=[]
						mylist.append(pre_morph["surface"])
						mylist.append(morph["surface"])
						pre_id = id(morph)
						pre_morph = morph
				





