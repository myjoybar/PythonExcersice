import requests
import re
import time
import urllib
import ssl
from bs4 import BeautifulSoup
import os

# https://segmentfault.com/a/1190000008360112
ssl._create_default_https_context = ssl._create_unverified_context #for douban

end = '&pager_offset=10'
urls = []
def getURLs(mainURL):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}
    html = requests.get(mainURL).text
    soup = BeautifulSoup(html, 'html.parser')
   # print(soup)
    picURL = re.findall('<img class.*?src="(.+?\.jpg)"', html, re.S)
    for url in picURL:
        urls.append(url)
        print(url)
    asoup = soup.select('.next a')[0]['href']
    print("asoup="+asoup)
    Next_page = 'http://www.dbmeinv.com' + asoup
    print("Next_page="+Next_page)
    if not end in asoup:
        getURLs(Next_page)
    else:
        print('链接已处理完毕！')
    return urls


def getImageName(imgUrl):
    lastSlashIndex = imgUrl.rfind('/')
    length = len(imgUrl)
    imageName = imgUrl[lastSlashIndex+1:length]
    print(imageName)
    return imageName

def mkdir(path):
    path = path.strip()
    path = path.rstrip("\\")
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        print(path+' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
        return False


def dowloadImage(realUrl):
    urllib.request.urlretrieve(realUrl, './saveimagedbmv/%s.jpg' % getImageName(realUrl))

def readFile(filePath):
    for line in open(filePath):
        url = line.strip().replace('\r','').replace('\n','').replace('\t','')
        if url.startswith('http'):
            print("start:"+url)
            urlList = getURLs(url)
            print("共有:" + str(len(urlList))+"张图片")
            for imageUrl in urlList:
                print(imageUrl)
                dowloadImage(imageUrl)

mkdir('./saveimagedbmv');
filePath = './doc/urlsdbmv.txt'
readFile(filePath)
print('图片下载完成')