import requests
import os
import requests
from bs4 import BeautifulSoup
# 文件、文件夹的移动、复制、删除、重命名

# 导入shutil模块和os模块
import shutil, os

# 复制整个目录(备份)
amount = 0
filePath = "/Users/joybar/Documents"
list = ['a2', 'a3', 'a4', 'b', 'b2', 'b3', 'b4','c', 'c2', 'c3', 'c4','d', 'd2', 'd3', 'd4']

listFile = [filePath+'/demo/a', filePath+'/demo1/a']

for indexSource,valueSource in enumerate(listFile):
    for indexTarget, valueTarget in enumerate(list):
        targetPath = valueSource[:-1] +valueTarget
        print("valueSource=" + valueSource + "  ,targetPath=" + targetPath)
        amount += 1;
        flag = os.path.exists(targetPath)
        if not flag:
            print("111=")
            shutil.copytree(valueSource, targetPath)



print("amount=" +  str(amount))

