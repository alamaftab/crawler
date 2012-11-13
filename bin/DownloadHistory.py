#!/usr/bin/python

from BeautifulSoup import BeautifulSoup
import re
import urllib2
import datetime
import time

configFile='c:/aftab/python/crawler/config/crawler.cfg'
execfile(configFile)
print crawlerData


stockSymbol='GRPN'

def parse_yahoo_history_url(stockSym_P,outputFilePath_P):

    url='http://finance.yahoo.com/q/hp?s=' + stockSym_P  + '+Historical+Prices'

    response = urllib2.urlopen(url)
    html = response.read()

    soup = BeautifulSoup(html)

    fileSuffix = datetime.datetime.today().strftime('%Y%m%d%H%M%S')
    outputFile=outputFilePath_P + "/out/" + stockSym_P  + "_" + "Hist" +  "_"  + fileSuffix  + ".txt"
    f = open(outputFile, 'w')
    
    for tablink in soup.findAll("td", {'class':re.compile("yfnc"),'nowrap':"nowrap" }):
        row=''
        for tt in tablink.parent.findAll("td"):
            row = row  + '|' + tt.text.replace(',','')
            
        f.write(row + "\n")
#       print row

    f.close()

##Main program begin from here##
################################
parse_yahoo_history_url( stockSymbol,   crawlerData)
    
    





                                                       
                                      
                                         

    



