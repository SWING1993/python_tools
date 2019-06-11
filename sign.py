#!/usr/bin/env python
# -*- coding: utf-8 -*
import requests
import json

def swing_sign_task():
    headers = {'Host': 'api.xiaoheihe.cn',
               'Accept': '*/*',
               'Cookie': 'pkey=MTU1MDczNzQ3OS4xOV82NjAyODU4b2lmbmpjb2poc2RjaWJxaw____;hkey=143597e3a2082b4c099cc0e4c9e14314',
               'User-Agent': 'xiaoheihe/1.1.53 (iPhone; iOS 12.1.2; Scale/3.00)',
               'Accept-Language': 'zh-Hans-US;q=1, en-US;q=0.9',
               'Referer': 'http://api.maxjia.com/'}
    api_url = "https://api.xiaoheihe.cn/task/sign/?lang=zh-cn&os_type=iOS&os_version=12.1.2&_time=1550737479&version=1.1.53&device_id=F6EC84D6-EBA5-41E0-9285-CBF6D8CB4500&heybox_id=6602858&hkey=005ceca8ce72a3794b9319f79433324c"
    r = requests.get(api_url, headers=headers)
    print r.text
    status = r.json()['status']
    msg = r.json()['msg']
    text = "SWING sign task " + status + " " + msg
    return text

def null_sign_task():
    headers = {'Host': 'api.xiaoheihe.cn',
               'Accept': '*/*',
               'Cookie': 'pkey=MTU1MTA2MjU5Ni4xMV8xNDYzMDk0N2d4bHZlbHV4dGltY2dtaG8__;hkey=fc1cd81ddbc5c3767ad4dfc4bd4cb430',
               'User-Agent': 'xiaoheihe/1.1.54 (iPad; iOS 11.3; Scale/2.00)',
               'Accept-Language': 'zh-Hans-CN;q=1',
               'Referer': 'http://api.maxjia.com/'}
    api_url = "https://api.xiaoheihe.cn/task/sign/?lang=zh-cn&os_type=iOS&os_version=11.3&_time=1551062596&version=1.1.54&device_id=953949AB-0FCB-43D4-8707-392B66288B9B&heybox_id=14630947&hkey=66a9d694c5aa269e47c844b7423e3da5"
    r = requests.get(api_url, headers=headers)
    print(r.text)
    status = r.json()['status']
    msg = r.json()['msg']
    text = "NULL sign task " + status  + " " + msg
    return text

def push_ding_msg(text):
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    api_url = "https://oapi.dingtalk.com/robot/send?access_token=15018194c2e2025afd72ff340a438fa445608eeecb1bf62f45816f5919760580"
    json_text = {
        "msgtype": "text",
        # "at": {
        #     "atMobiles": [
        #         "18667905583"
        #     ],
        #     "isAtAll": False
        # },
        "text": {
            "content": text
        }
    }
    requests.post(api_url, json.dumps(json_text), None, headers=headers)

def push_orange_msg(text):
    headers = {'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'}
    api_url = "http://118.24.216.163:8080/orange/message/send"
    json_text = {
        "messageToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOiIyIiwiZXhwIjoxNTU1NjUyNjI2fQ.MwZuRFzlOLEqKADVjQ5sHEvRBZxAxIzAQqsymOJvOYk",
        "title": "小黑盒签到",
        "content": text
    }
    requests.post(api_url, json_text, None, headers=headers)


msg_text = "小黑盒签到任务：\n" + swing_sign_task() + "\n" + null_sign_task()
push_ding_msg(msg_text)
push_orange_msg(msg_text)

