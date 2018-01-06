#!/usr/bin/env python
# coding=utf-8
import requests
import re
import urllib
import ssl
ssl._create_default_https_context = ssl._create_unverified_context #for douban

def getImageName(imgUrl):
    lastSlashIndex = imgUrl.rfind('/')
    length = len(imgUrl)
    imageName = imgUrl[lastSlashIndex+1:length]
    print(imageName)
    return imageName

def dowloadImage(realUrl):
    urllib.request.urlretrieve(realUrl, './saveimage/%s.jpg' % getImageName(realUrl))

def openUrl(url):
    try:
        response = requests.get(url, headers=headers, timeout=5)
        code = response.status_code
        html = response.text
       # print(html)
        reg = r'src="(.+?\.jpg)"'
        imgre = re.compile(reg)
        imglist = imgre.findall(html)
        print("有" + str(len(imglist)) + "张图片")
        for imgUrl in imglist:
            print("original imgUrl="+imgUrl)
            realUrl = "https:" + imgUrl
            if 'doubanio'in imgUrl:
                realUrl = imgUrl
           # print("real imgUrl=" + realUrl)
            dowloadImage(realUrl)
        if code == 200:
            print('可打开')
        else:
            print('不可打开')
    except Exception as e:
        print(e)
    return


def readFile(filePath):
    for line in open(filePath):
        url = line.strip().replace('\r','').replace('\n','').replace('\t','')
        if url.startswith('http'):
            print(url)
            openUrl(url)



# headers = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
url = "http://www.imooc.com/course/list"
# url = "http://item.taobao.com/item.htm?id=545036414066"
filePath = './doc/urls.txt'


readFile(filePath)


