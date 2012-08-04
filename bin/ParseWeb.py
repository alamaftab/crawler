from BeautifulSoup import BeautifulSoup
import re
import urllib2

f = open("test1.txt", 'w')

url = 'http://finance.yahoo.com/q/op?s=GRPN&m=2012-08'
response = urllib2.urlopen(url)
html = response.read()

soup = BeautifulSoup(html)

for tablink in soup.findAll("td", {'class':re.compile("yfnc"),'nowrap':"nowrap" }):
    row=''
    for tt in tablink.parent.findAll("td"):
        print tt.text
        row = row  + '|' + tt.text.replace(',','')
    print "------"
    print row
    f.write(row + "\n")

f.close()
    





                                                       
                                      
                                         





