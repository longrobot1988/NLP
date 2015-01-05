#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/06/10 15:43:57
#Author:Guo Weilong
"""
5つのファイル（英語のテキスト）にGENIA taggerを適用せよ。GENIA taggerは1分1行形式の入力を受け取るので、22のプログラム
を再利用せよ.また、入力ファイルはgzipで圧縮されていることに注意せよ。		
"""

import sys,re,glob
from geniatagger import *
tagger 	=	GeniaTagger(/Users/kubotanaoyuki/Desktop/NPL/geniatagger-python-0.1/geniatagger)

def main():
	for name in glob.glob('english_?.txt'):
		#逆方向から５番目から数える
		f1	=	open("71_GENIA_tagger_"+name[-5:],'w')
		print	"name",name
		for line in open(name):
			#両端のスペースを除去する	
			line	=	line.strip()
			#丸括弧の中にどのような正規表現があってもマッチし、
			#リストの最終要素として返されます。
			iList	=	re.split(r'(\.)([A-Z])|(\[[0-9]+\]+)([A-Z])',line)
			while None in iList: iList.remove(None)
			for w in range(len(iList)):
				w_tagger	=	None
				if w ==0 and len(iList) == 1 :
					w_tagger	=	tagger.parse(iList[w])
				elif w == 0:
					w2			=	list[w]
				elif w ==1:
					w2			=	w2 + ilist[w]
					w_tagger	=	tagger.parse(w2)
				elif w % 3 == 2:
					w2			=	iList[w]
				elif w == (len(iList)-1):
					w2 			=	w2 + iList[w]
					w_tagger	=	tagger.parse(w2)
				elif w % 3 == 0:
					w2			=	w2 + iList[w]
				else:
					w2			= 	w2 + iList[w]
					w_tagger	=	tagger.parse[w2]
				if w_tagger:
					for w in w_tagger:
						f1.write("\t".join(w)+"\n")
					f1.write("\n")
		f1.close()

if __name__ == '__main__':
	main()