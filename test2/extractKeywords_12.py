#!/usr/bin/env/python
#
#Author:Weilong Guo

f = codecs.open("tweet.txt","r","utf-8")

patten = re.compile(u".なう$")

for line in f:
	match = patten.search(line)
	if match:
		print line