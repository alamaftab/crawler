#!/usr/bin/python

from BeautifulSoup import BeautifulSoup
import re
import urllib2
import datetime
import time

configFile='c:/aftab/python/crawler/config/crawler.cfg'
execfile(configFile)
print crawlerData

inputDict={}


#Read input from crawlerData loop for every stock and innner loop for every date. Also download history.

def read_input_file(inputFile_P):
    fp=open(inputFile_P)

    for line in fp:
        lExpDt=[]
        for i,st in enumerate(line.split()):
            if i == 0:
                lStockSym=st
            else:
                lExpDt.append(st)

        inputDict[lStockSym]=lExpDt  
    
    fp.close()
#    print inputDict



stockSymbol='SHLD'
expDt='2012-08'

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
            row = row  + '|' + tt.text.replace(',','')
        f.write(row + "\n")

    f.close()

##Main program begin from here##
################################
read_input_file(crawlerData + '/in/stock.txt')
for key in inputDict.keys():
    for dt in inputDict[key]:
        parse_yahoo_option_url( key, dt,   crawlerData)
        
#parse_yahoo_option_url( stockSymbol, expDt,   crawlerData)
    
    





                                                       
                                      
                                         

    



