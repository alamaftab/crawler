#!/usr/bin/python

from BeautifulSoup import BeautifulSoup
import re
import urllib2

configFile='c:/aftab/python/crawler/config/crawler.cfg'
execfile('c:/aftab/python/crawler/config/crawler.cfg')
print crawlerData



#Read input from crawlerData loop for every stock and innner loop for every date. Also download history.

stockSymbol='GRPN'
expDt='2012-08'

def parse_yahoo_option_url(stockSym_P, expdt_P,outputFilePath_P):

    url = 'http://finance.yahoo.com/q/op?s=' + stockSym_P + '&m=' + expdt_P
    response = urllib2.urlopen(url)
    html = response.read()

    soup = BeautifulSoup(html)
    outputFile=outputFilePath_P + "/out/test1.txt"
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
    





                                                       
                                      
                                         

    



