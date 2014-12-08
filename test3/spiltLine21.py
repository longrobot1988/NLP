#!/usr/bin/env python
#-*-coding:utf-8-*-
#
#Author:Weilong Guo
#英語テキストを行に区切る			


import sys
import re

f = open("medline.txt","r")

for line in f:
    sent = line.split(".")

for s in sent:
    print s + "."