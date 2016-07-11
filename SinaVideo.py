# coding:UTF-8

from bs4 import BeautifulSoup
import re,os,glob

#path ="C:\\Users\\Hu Computer\\Desktop\\video"
path = "D:\\Users\\Administrator\\Desktop\\graduationProject\\gratu\\sites\\Sinavideo"
os.chdir(path)
SinaVideo = os.listdir(path)
if os.path.exists("SinaVideo.txt"):
    os.remove("SinaVideo.txt")
count = 1
fw= open("SinaVideo.txt",'w',encoding="utf-8")

for movie in SinaVideo:
    with open(movie,'r',encoding="utf-8") as file:
            html_doc = file.read().encode("utf-8").decode("utf-8")
            soup = BeautifulSoup(html_doc,"html.parser",from_encoding="utf-8")
            try:
                title = soup.title.text

                a = html_doc.find("<meta name=\"description\" content=\"")+34
                b = html_doc.find("<meta name=\"system\"")-5
                intro=html_doc[a:b]

                location=html_doc.find("swfOutsideUrl")
                url = html_doc[location+15:location+65]
                fw.write("insert into movie(moviename,introduction,url,fromwhere,type) values(")
                fw.write("\'")
                fw.write(title.replace("\'","").replace("\n","").replace(";",""))
                fw.write("\'")
                fw.write(',')
                fw.write("\'")
                fw.write(intro.strip().replace("\'","").replace("\n","").replace(";",""))
                fw.write("\'")
                fw.write(',')
                fw.write("\'")
                fw.write(url)
                fw.write("\'")
                fw.write(',')
                fw.write("\'视频\'")
                fw.write("\'")
                fw.write(',')
                fw.write("\'新闻\'")
                fw.write(");")
                fw.write('\n')
                print(count,title,'\n',intro,'\n',html_doc[location+15:location+65])
            except:
                print("error")
                print(count)
            count = count+1
