#coding:utf-8
import requests
from common.get_UserJwtToken import *

user_Agent = Get_Token_jwt().get_User_Agent()
xyx_jwt = Get_Token_jwt().get_xyx_jwt()
UserJwtToken = Get_Token_jwt().get_UserJwtToken()
url = "http://testdms.maxuscloud.cn/userService/current/authorizedApp"

h = {
    "User-Agent": user_Agent,
    "xyx_jwt":xyx_jwt,
    "UserJwtToken":UserJwtToken
}

r = requests.get(url,headers = h , verify = False)

print(r.text)