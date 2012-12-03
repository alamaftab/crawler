#!/usr/bin/python

from BeautifulSoup import BeautifulSoup
import string, sys, csv, re, __builtin__
import urllib2
import datetime
import time

configFile='c:/aftab/python/crawler/config/crawler.cfg'
execfile(configFile)
sys.path.append(crawlerHome +"/lib")

import ParseYahooFinanceWebLib

inputDict={}

##Main program begin from here##
################################
inputDict=ParseYahooFinanceWebLib.read_input_file(crawlerData + '/in/stock.txt')
for key in inputDict.keys():
    for dt in inputDict[key]:
        ParseYahooFinanceWebLib.parse_yahoo_option_url( key, dt,   crawlerData)
        




                                                       
                                      
                                         

    

        

    
