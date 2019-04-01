#!/usr/bin/env python
# -*- coding: utf-8 -*

import requests
import re
import urllib2
import json
import jsonpath

class Weather:
    date = ""
    text_day = ""
    code_day = ""
    text_night = ""
    code_night = ""
    high = ""
    low = ""


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
        "title": "杭州市天气预报",
        "content": text
    }
    requests.post(api_url, json_text, None, headers=headers)

# hearders = "User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) ApplewebKit/537.36 (Khtml, like Gecko) Chrome/60.0.3112.113 Safari/537.36"
# url = "https://tianqi.moji.com/weather/china/zhejiang/hangzhou"
# par = '(<meta name="description" content=")(.*?)(">)'
# opener = urllib2.build_opener()
# opener.addheaders = [hearders]
# urllib2.install_opener(opener)
# html = urllib2.urlopen(url).read().decode("utf-8")
# data = re.search(par,html).group(2)
# push_orange_msg(data)

def now_weather():
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    api_url = "https://api.seniverse.com/v3/weather/now.json?key=5g9hezbxwxfoo6ty&location=hangzhou&language=zh-Hans&unit=c"
    r = requests.get(api_url, headers=headers)
    if r.status_code == 200:
        json = r.json()
        return unicode("当前气温", "utf-8") + jsonpath.jsonpath(json, '$..temperature')[0]+ unicode("°C ", "utf-8") + jsonpath.jsonpath(json, '$..text')[0] + unicode("\n", "utf-8")
    return ""

def daily_weather():
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    api_url = "https://api.seniverse.com/v3/weather/daily.json?key=5g9hezbxwxfoo6ty&location=hangzhou&language=zh-Hans&unit=c&days=3"
    r = requests.get(api_url, headers=headers)
    print r.text
    if r.status_code == 200:
        json = r.json()
        d1 = unicode("今天：", "utf-8") + jsonpath.jsonpath(json, '$..low')[0] + unicode("°C到", "utf-8") + jsonpath.jsonpath(json, '$..high')[0] + unicode("°C ", "utf-8") + unicode("白天", "utf-8") + jsonpath.jsonpath(json, '$..text_day')[0] + unicode("，夜间", "utf-8") + jsonpath.jsonpath(json, '$..text_night')[0] + unicode("\n", "utf-8")
        d2 = unicode("明天：", "utf-8") + jsonpath.jsonpath(json, '$..low')[1] + unicode("°C到", "utf-8") + jsonpath.jsonpath(json, '$..high')[1] + unicode("°C ", "utf-8") + unicode("白天", "utf-8") + jsonpath.jsonpath(json, '$..text_day')[1] + unicode("，夜间", "utf-8") + jsonpath.jsonpath(json, '$..text_night')[1] + unicode("\n", "utf-8")
        d3 = unicode("后天：", "utf-8") + jsonpath.jsonpath(json, '$..low')[2] + unicode("°C到", "utf-8") + jsonpath.jsonpath(json, '$..high')[2] + unicode("°C ", "utf-8") + unicode("白天", "utf-8") + jsonpath.jsonpath(json, '$..text_day')[2] + unicode("，夜间", "utf-8") + jsonpath.jsonpath(json, '$..text_night')[2]
        return d1 + d2 + d3

    return ""

msg = now_weather() + daily_weather()
push_orange_msg(msg)
