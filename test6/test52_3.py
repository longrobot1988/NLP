#!/usr/bin/env python
#-*- coding:utf8 -*-
#
#Authour:Weilong Guo
#
#created on: 2014/12/6

import CaboCha,sys

from test51_1.py import cabochaParse

class Morph:
	def __init__(self,sentence):
		self.sentence		=	sentence
		self.CabochaResult	=	cabochaParse(sentence)
		self.paresMorphs  	=	[]
		


	def getparsedMorphs(self):
		return self.getParseMorphs

	def getSurfaces(self):
		return 

	def getBases(self):
		return [morph['srf'] for morph in self.getParseMorphs ]

	def getPoses(self):
		return[morph['pos'] for morph in self.getParseMorphs ]




if __name__ == '__main__':
	for line in sys.stdin.readlines():
		newMorph		=	Morph(line)
		print newMorph.getCabocharResult()
		print newMorph.getParseMorphs()
		print newMorph.getSurfaces()
		print newMorph.getposes()
		print newMorph.getPos1s()
		print newMoprh.getBases()