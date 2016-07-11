#encoding=utf-8
import re
import urllib2
import urllib
import json
import datetime
from bs4 import BeautifulSoup
import html5lib

html = open("singer.html","r").read()
soup = BeautifulSoup(html,"html.parser",from_encoding="utf-8")
a = soup.find_all("a")
count = 1
f = open("num.html","w")
for li in a[152:]:
    try:
        num = li.attrs["href"].split("/")
        title = li.attrs["title"]
        print count,num[2].encode("utf-8")
        f.write(num[2].encode("utf-8"))
        f.write("\n")
    except:
        print "err"

    count = count +1
f.close()
