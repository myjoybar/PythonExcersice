#!/usr/bin/python3
import requests

listTalkUUrl = ['http://talkyou.me/and/ff/en/a',
                'http://talkyou.me/and/ff/en/b',
                "http://talkyou.me/and/ff/en/c",
                "http://talkyou.me/and/ff/en/d",
                "http://talkyou.me/and/ff/en/e"];

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}

f = open("./doc/TalkUUrl.txt")
line = f.readline()
amount = 0
amountSuccess = 0
amountFailure = 0
while line:
    line = f.readline()
    if "http://talkyou.me/" in line:
        urlInfo = "URL" + str(amount) + ":" + line.strip()
        amount = amount + 1;
        try:
            response = requests.get(line.strip(), headers=headers, timeout=5)
            httpCode = response.status_code
            html = response.text
            if httpCode == 200:
                print(urlInfo + ':可打开')
                amountSuccess = amountSuccess + 1
            else:
                print(urlInfo + ':不可打开，' + str(httpCode))
                amountFailure = amountFailure + 1
        except Exception as e:
            print(e)

f.close()

print("总共有：" + str(amount) +"个 URL")
print("成功" + str(amountSuccess) +"个 URL")
print("失败" + str(amountFailure) +"个 URL")