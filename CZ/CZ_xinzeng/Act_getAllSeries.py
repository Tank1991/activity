import requests
import urllib3
urllib3.disable_warnings()
from common.Login_xyx.get_UserJwtToken import *
#新增页面获取所有车系
token = Get_Token_jwt().get_token()
jwt = Get_Token_jwt().get_jwt()
agent = Get_Token_jwt().get_User_Agent()

url = "https://test34.maxuscloud.cn/ampService/masterDataWebController/getAllSeries"

headers = {
    "User-Agent":agent,
    "xyx_jwt":jwt
}

r = requests.post(url,headers = headers ,verify = False)

print(r.text)








