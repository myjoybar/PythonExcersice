#!/usr/bin/python3
import requests
import os
import requests



headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}


amount = 0
amountSuccess = 0
amountFailure = 0
def openUrl(url):
    try:
        global amount
        global amountSuccess
        global amountFailure
        response = requests.get(url, headers=headers, timeout=5)
        httpCode = response.status_code
        html = response.text
        amount+=1
        if httpCode == 200:
            amountSuccess+=1
            print(url + ':可打开')
        else:
            amountFailure+=1
            print(url + ':不可打开，' + str(httpCode))
    except Exception as e:
        print(e)


def readFile(filePath):
    for line in open(filePath):
        if line.startswith('http://talkyou.me/'):
            url = line.strip().replace('\r', '').replace('\n', '').replace('\t', '')
            openUrl(url)



filePath = './doc/TalkUUrl.txt'
readFile(filePath)

print("总共有：" + str(amount) +"个 URL")
print("成功" + str(amountSuccess) +"个 URL")
print("失败" + str(amountFailure) +"个 URL")
