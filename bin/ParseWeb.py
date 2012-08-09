#!/usr/bin/python

from BeautifulSoup import BeautifulSoup
import re
import urllib2
import datetime
import time

configFile='c:/aftab/python/crawler/config/crawler.cfg'
execfile('c:/aftab/python/crawler/config/crawler.cfg')
print crawlerData

def read_input_file(inputFile_P):
    inputDict={}
    fp=open(inputFile_P)
    for i,st in enumerate(fp):
        print i
        print st

#Read input from crawlerData loop for every stock and innner loop for every date. Also download history.

stockSymbol='SHLD'
expDt='2012-09'

def parse_yahoo_option_url(stockSym_P, expdt_P,outputFilePath_P):

    url = 'http://finance.yahoo.com/q/op?s=' + stockSym_P  + '&m=' + expdt_P
    response = urllib2.urlopen(url)
    html = response.read()

    soup = BeautifulSoup(html)
    fileSuffix = datetime.datetime.today().strftime('%Y%m%d%H%M%S')
    outputFile=outputFilePath_P + "/out/" + stockSym_P  + "_" + expdt_P +  "_"  + fileSuffix  + ".txt"
    f = open(outputFile, 'w')
    for tablink in soup.findAll("td", {'class':re.compile("yfnc"),'nowrap':"nowrap" }):
        row=''
        for tt in tablink.parent.findAll("td"):
            print tt.text
            row = row  + '|' + tt.text.replace(',','')
        print "------"
        print row
        f.write(row + "\n")

    f.close()


parse_yahoo_option_url( stockSymbol, expDt,   crawlerData)
    





                                                       
                                      
                                         

    



