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
# filePath = "/Users/joybar/Documents/WorkSpaces/DingtoneWeb/Dingtone/and/fm"
filePath = "/Users/joybar/Documents/WorkSpaces/DingtoneWeb/Dingtone/ios/fm"
list = ['a1', 'a2', 'a3', 'b', 'b1', 'b2', 'b3','c', 'c1', 'c2', 'c3','d', 'd1', 'd2', 'd3','e', 'e1', 'e2', 'e3']

listCountry = ["/cn","/cnt","/en","/es","/fr","/pt","/tr"]
listAlreadySourceFile = ["/a","/b","/c","/d","/e"]
listTargetSourceIndex= ["1","2","3"]


for indexSourceCounty,country in enumerate(listCountry):
    for indexSource, valueSource in enumerate(listAlreadySourceFile):
        originalFilePath = filePath+country + valueSource
        print("===================")
        print("originalFilePath=" + originalFilePath )
        for indexTarget, valueTargetIndex in enumerate(listTargetSourceIndex):
            targetFilePath =  originalFilePath +valueTargetIndex
            print("targetFilePath=" + targetFilePath)
            amount+= 1;
            flag = os.path.exists(targetFilePath)
            if not flag:
                print("111=")
                successAmount += 1;
                shutil.copytree(originalFilePath, targetFilePath)



print("总共 amount=" +  str(amount))
print("成功 successAmount=" +  str(successAmount))

