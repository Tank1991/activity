import requests
import urllib3
urllib3.disable_warnings()
from common.Login_xyx.get_UserJwtToken import *
#通过orgId获取经销商战区信息
token = Get_Token_jwt().get_token()
jwt = Get_Token_jwt().get_jwt()
agent = Get_Token_jwt().get_User_Agent()

url  = "https://test34.maxuscloud.cn/ampService/masterDataWebController/queryChildOrgByOrgId"

headers = {
    "User-Agent":agent,
    "xyx_jwt":jwt,
    "Content-Type":"application/x-www-form-urlencoded"
}

body = {
   "orgId":"10012343"   # 10012343 经销商   10000003 战区
}

r = requests.post(url ,headers =headers ,data= body,verify=False)

result = r.json()
print(result)

