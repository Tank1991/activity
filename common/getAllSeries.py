#coding:utf-8
import requests
import urllib3
import json
from common.get_UserJwtToken import *
urllib3.disable_warnings()
'''
获取所有的车系
'''

user_Agent = Get_Token_jwt().get_User_Agent()
xyx_jwt = Get_Token_jwt().get_xyx_jwt()
UserJwtToken = Get_Token_jwt().get_UserJwtToken()
url = "http://testdms.maxuscloud.cn/ampService/masterDataWebController/getAllSeries"

headers = {
    "User-Agent":user_Agent,
    "xyx_jwt":xyx_jwt,
    "UserJwtToken":UserJwtToken,
    "Content-Type":"application/json;charset=UTF-8"
}

body ={
    "start":0,
    "length":5,
    "activityName":"",
    "activityType":10141001,
    "activityMode":"",
    "activityProperties":"",
    "beginTimeStart":"",
    "endTimeStart":"",
    "endTimeEnd":"",
    "stopTimeStart":"",
    "stopTimeEnd":"",
    "firstSource":"",
    "secondSource":"",
    "status":"",
    "approvalStatus":"",
    "activityCode":""
}
r = requests.post(url,verify = False,headers = headers)

result = r.text
print(result)





