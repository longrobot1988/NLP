#!/usr/bin/python
#-*-coding:utf-8-*-
#2015/1/25

import sys
from pymongo import Connection
import pymongo

con = Connection('127.0.0.1', 27017)
db = con.nlp100_kanouchi
col = db.tweets

q = unicode(sys.argv[1])

for data in col.find():
	if query in data["body"]:
		print "%s :\n%s" % (data["nickname"], data["body"])