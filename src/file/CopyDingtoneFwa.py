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
# filePath = "/Users/joybar/Documents/WorkSpaces/DingtoneWeb/Dingtone/and/fwa"
filePath = "/Users/joybar/Documents/WorkSpaces/DingtoneWeb/Dingtone/ios/fwa"
list = ['a1', 'a2', 'a3', 'b', 'b1', 'b2', 'b3','c', 'c1', 'c2', 'c3','d', 'd1', 'd2', 'd3','e', 'e1', 'e2', 'e3']





listFile = [filePath+'/cn/a', filePath+'/cnt/a', filePath+'/en/a', filePath+'/es/a', filePath+'/fr/a', filePath+'/pt/a', filePath+'/tr/a']

for indexSource,valueSource in enumerate(listFile):
    for indexTarget, valueTarget in enumerate(list):
        targetPath = valueSource[:-1] +valueTarget
        print("valueSource=" + valueSource + "  ,targetPath=" + targetPath)
        amount+= 1;
        flag = os.path.exists(targetPath)
        if not flag:
            print("111=")
            successAmount += 1;
            shutil.copytree(valueSource, targetPath)



print("总共 amount=" +  str(amount))
print("成功 successAmount=" +  str(successAmount))

