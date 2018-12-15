import requests
import urllib3
urllib3.disable_warnings()
from common.Login_xyx.get_UserJwtToken import *
#个人信息--已经通过
token = Get_Token_jwt().get_token()
jwt = Get_Token_jwt().get_jwt()
agent = Get_Token_jwt().get_User_Agent()

url = "https://test34.maxuscloud.cn/userService/current/userAndProxyInfo"

headers = {
    "User-Agent":agent,
    "xyx_jwt":jwt,
}

body = {}

r = requests.get(url,headers = headers ,verify = False)

result = r.json()
print(result)