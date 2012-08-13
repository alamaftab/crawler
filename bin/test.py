#!/usr/bin/python

from BeautifulSoup import BeautifulSoup
import re
import urllib2
import datetime
import time

inputFile_P='C:/aftab/python/crawler/data/in/stock.txt'

fp=open(inputFile_P)
inputDict={}
for line in fp:
    lExpDt=[]
    for i,st in enumerate(line.split()):
        if i == 0:
            lStockSym=st
        else:
            lExpDt.append(st)

    inputDict[lStockSym]=lExpDt  
    
    
fp.close()
for itm in inputDict.keys():
    print itm


#print 'test' + datetime.datetime.today().strftime('%Y%m%d%H%M%S')
#print 'test' + t

