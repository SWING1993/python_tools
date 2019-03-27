#!/usr/bin/env python
# -*- coding: utf-8 -*

import requests
import re
import urllib2
import json

def push_ding_msg(text):
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    api_url = "https://oapi.dingtalk.com/robot/send?access_token=7e6f02c3087edd19362340532a116a1f98d5b4310dba34685560598dc3803ccf"
    json_text= {
     "msgtype": "text",
        "at": {
            "atMobiles": [
                "18667905583"
            ],
            "isAtAll": False
        },
        "text": {
            "content": text
        }
    }
    print requests.post(api_url,json.dumps(json_text),headers=headers).content

def push_orange_msg(text):
    headers = {'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'}
    api_url = "http://118.24.216.163:8080/orange/message/send"
    json_text = {
        "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOiIyIiwiZXhwIjoxNTU1MDcyMDQ0fQ.hPfK8X0PM3IjnOWliBrq4OALRhvVgR3NFv0ROnteYfc",
        "title": "杭州天气预报",
        "content": text
    }
    requests.post(api_url, json_text, None, headers=headers)

hearders = "User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) ApplewebKit/537.36 (Khtml, like Gecko) Chrome/60.0.3112.113 Safari/537.36"
url = "https://tianqi.moji.com/weather/china/zhejiang/hangzhou"
par = '(<meta name="description" content=")(.*?)(">)'
opener = urllib2.build_opener()
opener.addheaders = [hearders]
urllib2.install_opener(opener)
html = urllib2.urlopen(url).read().decode("utf-8")
data = re.search(par,html).group(2)

push_orange_msg(data)
