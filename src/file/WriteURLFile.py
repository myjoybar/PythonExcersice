import requests
import os
import requests
from bs4 import BeautifulSoup
# 文件、文件夹的移动、复制、删除、重命名

# 导入shutil模块和os模块
import shutil, os

# 复制整个目录(备份)
successAmount = 0
amount = 0;
filePath = "http://talkyou.me/and/fm"

# filePath = "/Users/joybar/Documents/WorkSpaces/DingtoneWeb/Dingtone/ios/fm"

listCountry = ["/cn","/cnt","/en","/es","/fr","/pt","/tr"]
listAlreadySourceFile = ["/a","/b","/c","/d","/e"]
listTargetSourceIndex= ["","1","2","3"]

listURL = []          ## 空列表

def loopList(list):
    for value in list:
        print("value=" + value)

#创建文件夹
def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        print("创建文件夹")
        os.makedirs(path)
    else:
        print("文件夹已经存在")

def mkFile(path,fileName):
    exists = os.path.exists(path+fileName)
    if not exists:
        print("创建文件")
        file = open(path+fileName, 'w')
        file.close()
    else:
        print("文件已经存在")

def writeFile(path,fileName):
    mkFile(path,fileName)
    f = open(path+fileName, "a+")
    for value in listURL:
        print("value=" + value)
        f.writelines(value + "\n")
    f.close()




for indexSourceCounty,country in enumerate(listCountry):
    listURL.append("========")
    for indexSource, valueSource in enumerate(listAlreadySourceFile):
        originalFilePath = filePath+country + valueSource
        print("===================")
        print("originalFilePath=" + originalFilePath )
        listURL.append("  ")
        for indexTarget, valueTargetIndex in enumerate(listTargetSourceIndex):
            targetFilePath =  originalFilePath +valueTargetIndex
            print("targetFilePath=" + targetFilePath)
            listURL.append(targetFilePath)
            amount+= 1;



loopList(listURL)
print("总共 amount=" +  str(amount))
print("成功 successAmount=" +  str(successAmount))


file = "url.txt"
# mkdir(file)
# mkFile("",file)
writeFile("",file)

