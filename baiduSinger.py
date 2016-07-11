#encoding=utf-8
import re
import urllib2
import urllib
import json
import datetime
from bs4 import BeautifulSoup
import html5lib

'''
html = open("singer.html","r").read()
soup = BeautifulSoup(html,"html.parser",from_encoding="utf-8")
a = soup.find_all("a")
count = 1
f = open("a.html","w")
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

'''
"""
        formdata = { "songIds" : ",".join(sids)}
        data_encoded = urllib.urlencode(formdata)
        songList = urllib2.urlopen(SONG_LINK_URL,data_encoded)
        songListJson = songList.read()
        js = json.loads(songListJson)
        for music in js["data"]["songList"]:
            songName = music["songName"]
            artistName = music["artistName"]
            format = music["format"]

            albumName =music["albumName"]
            time = music["time"]
            rate = music["rate"]
            size = music["size"]
            lrcLink = music["lrcLink"]
            songLink = music["songLink"]
            showLink = music["showLink"]
            print songName
"""
def get_html(url):
    res = urllib2.urlopen(url)
    js = json.loads(res.read().decode("utf-8"))
    return js["data"]["html"]

def deal_song_sid(data):
    sids = []
    sidPattern = re.findall("&quot;sid&quot;:.*?,&quot;",data)
    for sid in sidPattern:
        #sids.append(re.sub(',&quot;','',re.sub('&quot;sid&quot;:','',sid)))
        sids.append(re.sub('&quot;,&quot;','',re.sub('&quot;sid&quot;:&quot;','',sid)))
    sids1 = []
    for s in sids:
        if "&quot;" in s:
            a = re.sub("&quot;","",s)
            sids1.append(a)
        else:
            sids1.append(s)
    return sids1

def get_song(sids):
    if len(sids) == 0:
        return 1
    formdata = { "songIds" : ",".join(sids)}
    data_encoded = urllib.urlencode(formdata)
    songList = urllib2.urlopen(SONG_LINK_URL,data_encoded)
    songListJson = songList.read()
    js = json.loads(songListJson)
    global co
    songDetail = {}
    for music in js["data"]["songList"]:
            songDetail["songName"] = music["songName"].encode("utf-8")
            songDetail["artistName"] = music["artistName"].encode("utf-8")
            songDetail["format"] = music["format"].encode("utf-8")
            songDetail["albumName"] =music["albumName"].encode("utf-8").replace("("," ").replace(")"," ").replace("\'"," ").replace(","," ")
            songDetail["mins"] = str(music["time"])
            songDetail["rate"] = str(music["rate"])
            #songDetail["size"] = music["size"]
            #songDetail["lrcLink"] = music["lrcLink"].encode("utf-8")
            songDetail["songLink"] = music["songLink"].encode("utf-8")
            songDetail["showLink"] = music["showLink"].encode("utf-8")
            print co,songDetail["songName"]+'-'+songDetail["artistName"]+'.'+songDetail["format"]
            #json.dump(songDetail,open("music.json","a"))
            f.write("insert into movie(songname,artist,url,mins,rate,fromwhere,album) values(")
            f.write("\'"+songDetail["songName"].replace("\'","")+'\',\''+songDetail["artistName"].replace("\'","")+'\',\''+songDetail["songLink"]+'\',\''+songDetail["mins"]+'\',\''+songDetail["rate"]+'\',\''+'音乐'+'\',\''+songDetail["albumName"]+"\');")
            f.write("\n")
            co +=1
    #return songDetail

if __name__ == '__main__':
    SONG_LINK_URL = 'http://play.baidu.com/data/music/songlink'
    SINGER_LINK ='http://music.baidu.com/artist/'

    start = datetime.datetime.now()
    co =1

    fw = open("num.html","r")
    f = open("MusciBaiduJSON.txt","w")
    line = fw.readlines()
    for li in line:
        try:
            res = urllib.urlopen(SINGER_LINK+li)
            html_singer = res.read().decode("utf-8")
            for i in range(0,5000,25):
                url = "http://music.baidu.com/data/user/getsongs?start="+unicode(i)+"&ting_uid="+li.strip("\n")+"&order=hot&hotmax=0&pay=&.r=0.51852875558095391465026416740"

                data = get_html(url)
                sids = deal_song_sid(data)
                songDetail = get_song(sids)
                if get_song(sids) == 1:
                    break
                print datetime.datetime.now() - start
        except:
            print "error"
    fw.close()
    f.close()