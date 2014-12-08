
#!/usr/bin/env python
#-*- coding:utf8 -*-

#
#Author:Weilong GUO
#

import sys
import marshal

f = open("inflection.table.txt","r")
output = open("dictionary_1.txt","w")

dic = {}
for line in f:
	words = line.strip().split("|")
	dic[words[0]]  = (words[1],words[3],words[6])
	
marshal.dump(dic,output)
#開かれたファイルに値を書き込む。	
	
f.close()
output.close()

