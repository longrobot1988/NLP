#!/usr/bin/env python
#-*- coding:utf8 -*-
#
#Authour:Weilong Guo
#

if __name__ == '__main__':
	
	import import_from
	testclass1	=	import_from.testclass()
	testclass1.testmethod("1")

	from import_from import testclass
	testclass2	=	testclass()
	testclass2.testmethod("2")