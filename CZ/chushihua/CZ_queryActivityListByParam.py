import requests
import urllib3
urllib3.disable_warnings()
from common.Login_xyx.get_UserJwtToken import *
#车展活动列表查询--已经通过
token = Get_Token_jwt().get_token()
jwt = Get_Token_jwt().get_jwt()
agent = Get_Token_jwt().get_User_Agent()
url = "https://test34.maxuscloud.cn/ampService/activityWebController/queryActivityListByParam"

headers = {
    "User-Agent":agent,
    "xyx_jwt":jwt,
    "Content-Type":"application/json;charset=UTF-8"
}

body = {"start":0,"length":5,"activityType":10141002}

r = requests.post(url ,headers =headers ,json= body,verify=False)

result = r.json()

print(result)













