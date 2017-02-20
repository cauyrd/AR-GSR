#!/usr/bin/python
#-*- coding: utf-8 -*-
#===============================================================================
#
#         FILE: test.py
#
#        USAGE: ./test.py  
#
#  DESCRIPTION: 
#
#      OPTIONS: ---
# REQUIREMENTS: ---
#         BUGS: ---
#        NOTES: ---
#       AUTHOR: Rendong Yang (cauyrd@gmail.com), 
# ORGANIZATION: 
#      VERSION: 1.0
#      CREATED: Wed Apr 30 13:27:17 CDT 2014
#     REVISION: ---
#===============================================================================
import sys
import numpy as np
normal_ratio = 1.19308943089
ifp = open(sys.argv[1]+'.cov.bed')
region = {}
for line in ifp:
	items = line.rstrip().split()
	try:
		region[items[3]].append(int(items[-1]))
	except KeyError:
		region[items[3]] = [int(items[-1])]
ifp.close()
ar_zero = sum(x==0 for x in region['AR'])
ar_covered = len(region['AR'])-ar_zero
for each in region:
	region[each] = sum(region[each])/len(region[each])
ratio = region['AR']/np.median([region['CONTROL1']/2,region['CONTROL2'],region['CONTROL3']/2,region['CONTROL4']/2,region['CONTROL5']/2])

print sys.argv[1][:8]+'\t'+str(region['AR'])+'\t'+str(int(round(ratio/normal_ratio)))+'\t'+str(ar_zero)+'/'+str(ar_covered)
