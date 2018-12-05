#coding:utf-8
import requests
from common.get_UserJwtToken import *
import  json
user_Agent = Get_Token_jwt().get_User_Agent()
xyx_jwt = Get_Token_jwt().get_xyx_jwt()
UserJwtToken = Get_Token_jwt().get_UserJwtToken()

url = "http://testdms.maxuscloud.cn/userService/current/userVO"

h = {
    "User-Agent": user_Agent,
    "xyx_jwt":xyx_jwt,
    "UserJwtToken":UserJwtToken
}

r = requests.get(url,headers = h , verify = False)

print(json.loads(r.text))