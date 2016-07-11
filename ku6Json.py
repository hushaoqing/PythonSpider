# coding:utf-8
from bs4 import BeautifulSoup
import re,os,glob
import json
import urllib.request

#path ="C:\\Users\\Hu Computer\\Desktop\\ku6video"
path = "D:\\Users\\Administrator\\Desktop\\graduationProject\\gratu\\sites\\ku6video"
os.chdir(path)
if os.path.exists("ku6.txt"):
    os.remove("ku6.txt")
movielist = os.listdir(path)
count = 1
fw= open("ku6.txt",'w',encoding="utf-8")
for movie in movielist:
    with open(movie,'rb') as file:
        html_doc = file.read()

        soup = BeautifulSoup(html_doc,"html.parser",from_encoding="utf-8")
        keyall = soup.find_all("a",class_="plus")
        for a in keyall:
            print(count)
            print(a.attrs["href"].split("#")[1])
            key = a.attrs["href"].split("#")[1]
            url = "http://v.ku6.com/fetchVideo4Player/"+key+".html"
            resp = urllib.request.urlopen(url)
            js= json.loads(resp.read().decode('utf-8'))
            try:
                title = js["data"]["t"]
                pic = js["data"]["picpath"]
                url = js["data"]["f"]
                fw.write("insert into movie(moviename,pic,url,fromwhere,type) values(")
                fw.write("\'"+title.replace("\'","").replace("\n","").replace(";","")+"\'")
                fw.write(",")
                fw.write("\'"+pic+"\'")
                fw.write(",")
                fw.write("\'"+url+"\'"+","+"\'"+"视频"+"\'"+","+"\'"+"娱乐"+"\'")
                fw.write(");")
                fw.write("\n")
                print(js["data"]["t"],js["data"]["picpath"],js["data"]["f"])
            except:
                print(count,"error")
            count = count+1

