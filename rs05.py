'''
__author__ = 'Hu Computer'

def txt_wrap_by(start_str, end, html):
    start = html.find(start_str)
    if start >= 0:
        start += len(start_str)
        end = html.find(end, start)
        if end >= 0:
            return html[start:end].strip()

if __name__=="__main__":
            print(txt_wrap_by("《","》","《中国》"))
'''
from bs4 import BeautifulSoup
import urllib.request
import re

def deal_error(error):
    try:
        error
    except:
        f.write("")

def htmlparser(file):
            global count
            a = "◎"
            html_doc = file
            if a not in html_doc:
                #print(count)
                soup = BeautifulSoup(html_doc,"html.parser",from_encoding="utf-8")
                moviename = soup.find("h1").get_text()
                introduction = soup.find("div",class_="info").get_text()
                director = re.search('导演:(.*?)(<br[ ]{0,1}/>)',html_doc)
                scriptwriter =  re.search('编剧:(.*?)(<br[ ]{0,1}/>)',html_doc)
                type = re.search('类型:(.*?)(<br[ ]{0,1}/>)',html_doc)
                langu = re.search('语言: (.*?)(<br[ ]{0,1}/>)',html_doc)
                released = re.search('上映日期: (.*?)(<br[ ]{0,1}/>)',html_doc)
                mins = re.search('片长:(.*?)(<br[ ]{0,1}/>)',html_doc)
                actor = re.search('主演:(.*?)(<br[ ]{0,1}/>)',html_doc)
                url = soup.find("div",class_="detail").find("a",target="_self")
                count = count + 1
            else:
               # print(count)
                soup = BeautifulSoup(html_doc,"html.parser",from_encoding="utf-8")
                moviename = soup.find("h1").get_text()
                introduction = soup.find("div",class_="info").get_text()
                director = re.search('◎导　　演(.*?)(<br[ ]{0,1}/>)',html_doc)
                scriptwriter =  re.search('编剧:(.*?)(<br[ ]{0,1}/>)',html_doc)
                type = re.search('(◎类　　型)(.*?)(<br[ ]{0,1}/>)',html_doc)
                langu = re.search('◎语　　言 (.*?)(<br[ ]{0,1}/>)',html_doc)
                released = re.search('上映日期: (.*?)(<br[ ]{0,1}/>)',html_doc)
                mins = re.search('◎片　　长(.*?)(<br[ ]{0,1}/>)',html_doc)
                actor = re.search('◎主　　演(.*?)(<br[ ]{0,1}/>)',html_doc)
                url = soup.find("div",class_="detail").find("a",target="_self")
                count = count + 1


            if moviename:print(count,moviename)

            '''
            if introduction:
                print(introduction,'\n')
            if url:
                print(url,'\n')
            if director:
                dire = re.compile(';')
                ddd = dire.sub(' ',director.group(1))
                print("导演：",ddd.strip(),'\n')
            if scriptwriter:print("编剧：",scriptwriter.group(1).strip(),'\n')
            if type:print("类型：",type.group(1).strip(),'\n')
            if langu:print("语言：",langu.group(1).strip(),'\n')
            if released:print("上映日期：",released.group(1).strip(),'\n')
            if mins:print("片长：",mins.group(1).strip(),'\n')
            if actor:
                dire = re.compile(';')
                ddd = dire.sub(' ',actor.group(1))
                A = re.compile('\'')
                B = A.sub(' ',ddd)
                print(B.strip())
            '''
            f.write("insert into movie(moviename,introduction,director,scriptwriter,type,langu,released,mins,actor,url) VALUES (")
            f.write("\'")
            if moviename:
                try:
                    f.write(str(moviename).replace("\'",""))
                except:
                    f.write("")
            f.write("\',")
            f.write("\'")
            if introduction :
                    #A = re.compile('\'')
                    #B = A.sub(' ',introduction)
                    #in1 = re.compile(';')
                    #b = in1.sub('  ',B)
                    try:
                        f.write(str(introduction).replace("\'","").replace(";","").replace("\n",""))
                    except:
                        f.write("")
            f.write("\',")
            f.write("\'")
            if director:
                    #A = re.compile('\'')
                    #B = A.sub(' ',director.group(1))
                    #a = re.compile(';')
                    #b = a.sub(' ',B)
                    try:
                        f.write(director.group(1).replace("\'","").replace(";","").replace("\n","").replace("&middot","").strip())
                    except:
                        f.write("")
            f.write("\',")
            f.write("\'")
            if scriptwriter :
                    #A = re.compile('\'')
                    #B = A.sub(' ',scriptwriter.group(1))
                    #a = re.compile(';')
                    #b = a.sub(' ',B)
                    try:
                        f.write(scriptwriter.group(1).replace("\'","").replace(";","").replace("\n","").replace("&middot","").strip())
                    except:
                        f.write("")
            f.write("\',")
            f.write("\'")
            if type:
                try:
                    f.write(type.group(1).replace("\'","").replace(";","").replace("\n","").strip())
                except:
                    f.write("")
            f.write("\',")
            f.write("\'")
            if langu:
                try:
                    f.write(langu.group(1).strip())
                except:
                    f.write("")
            f.write("\',")
            f.write("\'")
            if released:
                rel = list(filter(lambda cn:cn in "1234567890-",released.group(1)[0:10]))
                stra = ''.join(rel)
                f.write(stra)
            f.write("\',")
            f.write("\'")
            if mins:
                scon = list(filter(str.isdigit,mins.group(1)[0:4]))
                str_convert = ''.join(scon)
                f.write(str_convert)
            f.write("\',")
            f.write("\'")
            if actor:
                    #A = re.compile('\'')
                    #B = A.sub(' ',actor.group(1))
                    #a = re.compile(';')
                    #b = a.sub(' ',B)
                    try:
                        f.write(actor.group(1).replace("\'","").replace(";","").replace("\n","").replace("&middot","").strip())
                    except:
                        f.write("")
            f.write("\',")
            f.write("\'")
            if url:
                try:
                    f.write(str(url.attrs['href']).replace("\'","\\'"))
                except:
                    f.write("")
            f.write("\'")
            f.write(")")
            f.write(";")
            f.write('\n')

            return

def detail(de):
    global num
    res = urllib.request.urlopen(de)
    html =res.read().decode("utf-8")
    htmlparser(html)

    return
'''
    try:
        name = soup.find("h1")
        link = soup.find("div",class_="detail").find_all("a",target="_self")
        link2 = soup.find("div",class_="detail").find("a")
        f.write(str(num)+name.get_text()+'\n')
        print(num,name.get_text())
        for a in link:
            print("迅雷链接：",a.attrs["href"])
            f.write("迅雷链接："+a.attrs["href"]+'\n')
        code = html.find("密码")
        code1 = html[code+3:code+8]
        if "http://pan.baidu.com/s" in link2.attrs["href"]:
            f.write("百度云："+link2.attrs["href"]+"密码："+code1.strip('<')+'\n')
            print("百度云：",link2.attrs["href"],"密码：",code1.strip('<'))
        link3 = soup.find("div",class_="resources").find_all("a")
        for l in link3:
            if l.attrs["href"] is not "#":
                f.write("迅雷链接："+l.attrs["href"])
                print(l.attrs["href"]+'\n')
    except:
        print("NO LINK!")
    num +=1
'''



def first(url):
    res = urllib.request.urlopen(url)
    html =res.read().decode("utf-8")
    soup = BeautifulSoup(html,"html.parser",from_encoding="utf-8")
    namelist = soup.find("ul",class_="movie-list reset").find_all("a",class_="pic fl")
    for i in namelist:
       de = "http://www.rs05.com/"+str(i.attrs["href"])
       detail(de)

if __name__ == '__main__':
    f = open("rs05Test.txt","w")
    count = 0
    for i in range(1,1917):

        url = "http://www.rs05.com/"+str(i)

        first(url)

    f.close()
