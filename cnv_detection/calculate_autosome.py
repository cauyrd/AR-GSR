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
ar_normal_ratio = 1.19308943089
#rb1_normal_ratio = 1.16338582677
#tp53_normal_ratio = 1.16338582677
#rb1_normal_ratio = 0.581692913386
#tp53_normal_ratio = 0.581692913386
rb1_normal_ratio = float(sys.argv[2])
tp53_normal_ratio = float(sys.argv[3])
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
rb1_zero = sum(x==0 for x in region['RB1'])
rb1_covered = len(region['RB1'])-rb1_zero
tp53_zero = sum(x==0 for x in region['TP53'])
tp53_covered = len(region['TP53'])-tp53_zero
for each in region:
	region[each] = sum(region[each])/len(region[each])
ar_ratio = region['AR']/np.median([region['CONTROL1']/2,region['CONTROL2'],region['CONTROL3']/2,region['CONTROL4']/2,region['CONTROL5']/2])
rb1_ratio = region['RB1']/np.median([region['CONTROL1'],region['CONTROL2']*2,region['CONTROL3'],region['CONTROL4'],region['CONTROL5']])
tp53_ratio = region['TP53']/np.median([region['CONTROL1'],region['CONTROL2']*2,region['CONTROL3'],region['CONTROL4'],region['CONTROL5']])
print sys.argv[1][:8]+'\tAR\t'+str(region['AR'])+'\t'+str(int(round(ar_ratio/ar_normal_ratio)))+'\t'+str(ar_zero)+'/'+str(ar_covered)+'\tRB1\t'+str(region['RB1'])+'\t'+str(int(round(2*rb1_ratio/rb1_normal_ratio)))+'\t'+str(rb1_zero)+'/'+str(rb1_covered)+'\tTP53\t'+str(region['TP53'])+'\t'+str(int(round(2*tp53_ratio/tp53_normal_ratio)))+'\t'+str(tp53_zero)+'/'+str(tp53_covered)
#print rb1_ratio,tp53_ratio
