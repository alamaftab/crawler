#!/usr/bin/python

from BeautifulSoup import BeautifulSoup
import re,  __builtin__
import urllib2
import datetime
import time

configFile='c:/aftab/python/crawler/config/crawler.cfg'
execfile(configFile)

#Read input from crawlerData loop for every stock and innner loop for every date. Also download history.

def read_input_file(inputFile_P):
    inputDict={}
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
    return inputDict
#    print inputDict        



def parse_yahoo_option_url(stockSym_P, expdt_P,outputFilePath_P):

    url = 'http://finance.yahoo.com/q/op?s=' + stockSym_P  + '&m=' + expdt_P
    response = urllib2.urlopen(url)
    html = response.read()

    soup = BeautifulSoup(html)
    fileSuffix = datetime.datetime.today().strftime('%Y%m%d%H%M%S')
    fileDate = datetime.datetime.today().strftime('%Y%m%d')
    fileTime = datetime.datetime.today().strftime('%H%M%S')
    
    outputFile=outputFilePath_P + "/out/" + stockSym_P + "/" + "OPT/" + stockSym_P  + "_" + expdt_P +  "_"  + fileSuffix  + ".txt"
    f = open(outputFile, 'w')   
#   git stock ticker price
    stkTickerPrice = soup.findAll("span", {'class':re.compile("time_rtq_ticker") })[0].findAll("span")[0].text

#   Logic for reading option price
    for tablink in soup.findAll("td", {'class':re.compile("yfnc"),'nowrap':"nowrap" }):
        row=''
        for tt in tablink.parent.findAll("td"):
            row = row  + '|' + tt.text.replace(',','')

# format the row for writing to the file.
        
        IsPutCall='P'
        if re.match(r'(.)*[0-9]C[0-9](.)*',row):    
            IsPutCall='C'

        out2 = re.search(r'([0-9][0-9][0-9][0-9][0-9][0-9])([CP])',row)
        strikeDt_full = out2.group(1)

            
        row = stockSym_P + '|' + fileDate  + '|' + fileTime + '|' + strikeDt_full + '|' + IsPutCall  + '|' + stkTickerPrice  + row
        f.write(row + "\n")

    f.close()


#function for downloading historical data
 
def parse_yahoo_history_url(stockSym_P,outputFilePath_P):

    url='http://finance.yahoo.com/q/hp?s=' + stockSym_P  + '+Historical+Prices'

    response = urllib2.urlopen(url)
    html = response.read()

    soup = BeautifulSoup(html)

    fileSuffix = datetime.datetime.today().strftime('%Y%m%d%H%M%S')
    outputFile=outputFilePath_P + "/out/" + stockSym_P + "/" + "HIST/" + stockSym_P   + "_" + "Hist" +  "_"  + fileSuffix  + ".txt"
    f = open(outputFile, 'w')
    
    for tablink in soup.findAll("td", {'class':re.compile("yfnc"),'nowrap':"nowrap" }):
        row=''
        for tt in tablink.parent.findAll("td"):
            tt_str=tt.text.replace(',','')
            if re.search(r'([0-9]* [0-9][0-9][0-9][0-9])',tt.text.replace(',','')):
                kk= time.strptime(tt.text.replace(',',''), "%b %d %Y")
                tt_str=__builtin__.str(kk.tm_year*10000 + kk.tm_mon*100 + kk.tm_mday)

            row = row  + '|' + tt_str
            
        f.write(row + "\n")
#       print row

    f.close()   
    

#### End of function ########



                                                       
                                      
                                         

    



