import requests
import urllib3
urllib3.disable_warnings()
from common.Login_xyx.get_UserJwtToken import *
#车展活动的潜客目标数量--已经通过
token = Get_Token_jwt().get_token()
jwt = Get_Token_jwt().get_jwt()
agent = Get_Token_jwt().get_User_Agent()

url = "https://test34.maxuscloud.cn/ampService/actClmEffLeadsDetailController/queryActClmEffLeadsDetialList"

headers = {
    "User-Agent":agent,
    "xyx_jwt":jwt,
    "Content-Type":"application/x-www-form-urlencoded"
}

body = {
    "activityCode":"Maxus-CZ-201812-0010"
}

r = requests.post(url ,headers =headers ,data= body,verify=False)

result = r.json()
print(result)