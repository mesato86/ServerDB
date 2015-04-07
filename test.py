#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import walk 

jsonpath = "/home/alex/Documents/ServerDB/1"
imglist = []
jsonlist = []
jsonlistcomp = []
imglistcomp = []

def JImport():
	
	global imglist
	global jsonlist
	global jsonlistcomp
	global imglistcomp
		

	for (dirpath, dirnames, filenames) in walk(jsonpath):
		for item in filenames:
			if item[-3:] == "son":
				jsonlist.append(item)
				jsonlistcomp.append(item[:-5])
				
			if item[-3:] == "jpg":
				imglist.append(item)
				imglistcomp.append(item[:-4])
	#print len(imglistcomp)
	#print len(jsonlistcomp)
	#print imglistcomp
	#print jsonlistcomp
			
	s = set(jsonlistcomp)
	miss = [x for x in imglistcomp if x not in s]
	print "missing json", miss
	
	s = set(imglistcomp)
	miss = [x for x in jsonlistcomp if x not in s]
	print "missing jpg", miss
	
	return
	


def jimg():
	

	imglist = JImport()
	
	for filename in imglist:
		with open(jsonpath+filename) as data_file:
			data = json.load(data_file)
		
			print data["bio_para"]["BIO17: Precipitation of Driest Quarter"]
			
JImport()
	
