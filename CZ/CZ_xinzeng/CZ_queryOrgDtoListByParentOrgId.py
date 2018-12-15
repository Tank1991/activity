import requests
import urllib3
urllib3.disable_warnings()
from common.Login_xyx.get_UserJwtToken import *
#车展新增战区对应的战区/大区/小区--已经通过
token = Get_Token_jwt().get_token()
jwt = Get_Token_jwt().get_jwt()
agent = Get_Token_jwt().get_User_Agent()

url = "https://test34.maxuscloud.cn/ampService/masterDataWebController/queryOrgDtoListByParentOrgId"

headers = {
    "User-Agent":agent,
    "xyx_jwt":jwt,
    "Content-Type":"application/x-www-form-urlencoded"
}

body = {
    "orgId":"10000003"
}

r = requests.post(url ,headers =headers ,data= body,verify=False)

result = r.json()
print(result)






