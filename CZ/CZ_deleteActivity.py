import requests
import urllib3
urllib3.disable_warnings()
from common.Login_xyx.get_UserJwtToken import *
#车展的删除按钮,传活动的ID
token = Get_Token_jwt().get_token()
jwt = Get_Token_jwt().get_jwt()
agent = Get_Token_jwt().get_User_Agent()

url = "https://test34.maxuscloud.cn/ampService/activityWebController/deleteActivity"

headers = {
    "User-Agent":agent,
    "xyx_jwt":jwt,
    "Content-Type":"application/x-www-form-urlencoded"
}
body ={
    "activityId":"10000000033299"
}

r = requests.post(url,headers = headers,data = body,verify = False)

result = r.text
print(result)