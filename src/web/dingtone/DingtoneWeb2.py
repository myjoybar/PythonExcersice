#!/usr/bin/python3
import requests
listTalkUUrl = ['http://talkyou.me/and/ff/en/a',
         'http://talkyou.me/and/ff/en/b',
         "http://talkyou.me/and/ff/en/c",
         "http://talkyou.me/and/ff/en/d",
         "http://talkyou.me/and/ff/en/e"];

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}

for i in range(len(listTalkUUrl)):
    url = listTalkUUrl[i]
    urlInfo = "URL" +str(i)+":"+ url
    try:
        response = requests.get(url, headers=headers, timeout=5)
        httpCode = response.status_code
        html = response.text
        # print(html)
        if httpCode == 200:
            print(urlInfo+':可打开')
        else:
            print(urlInfo + ':不可打开，'+str(httpCode))
    except Exception as e:
        print(e)