#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
from sys import argv
import re 
import time

script, filename = argv
METHOD_AS_RE = 'GET |POST |DELETE |HEAD |OPTIONS |PUT |\?| HTTP|\n'

try : 		
	file_name=open(filename)
	urldict = {}
	urltime={}
	for i in file_name:
		urls = re.split(METHOD_AS_RE,i)[1]				
		times = re.split(' ~ |\n',i)[1]
		if not times=="-" :		
			time=float(times)
		else :
			time = None		
		urldict[urls] = urldict.get(urls,0)+1

		if time>urltime.get(urls, 0):
			urltime.update({urls: time})
	# MTC = Most Time Consuming & MRU = Max Requested URL
	MTC = max(urltime, key=urltime.get)
	MRU = max(urldict, key=urldict.get)

	print "*"*80,"\n"
	print "Distinct URL Count is %s .\n" % len(urldict)
	print "Most Time Consuming URL is -> %s , and it is executed in %s sec.\n" % (MTC,urltime[MTC])
	print "Most Requested URL is -> %s , and it is appeared %s times.\n" % (MRU,urldict[MRU]) 
	print "*"*80

	file_name.close()
except IOError :	
	print "no such a file named : %s" %filename 
