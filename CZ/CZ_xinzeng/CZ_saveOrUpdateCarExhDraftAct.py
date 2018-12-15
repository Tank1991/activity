import requests
import urllib3
urllib3.disable_warnings()
from common.Login_xyx.get_UserJwtToken import *
#新增车展活动--已经通过
token = Get_Token_jwt().get_token()
jwt = Get_Token_jwt().get_jwt()
agent = Get_Token_jwt().get_User_Agent()

url = "https://test34.maxuscloud.cn/ampService/actCarExhInfoWebController/saveOrUpdateCarExhDraftAct"

headers = {
    "User-Agent":agent,
    "xyx_jwt":jwt,
    "Content-Type":"application/json;charset=UTF-8"
}

body = {
    "activityDto":{
        "id":"",
        "activityName":"删除的哈",
        "activityType":10141002,
        "activityMode":"RV80B,T60,MV80,EV80,G10,V80,EG10",
        "firstSource":10000000000002,
        "secondSource":10000000000006,
        "content":"接口的活动简述",
        "beginTimeString":"2018-12-01",
        "endTimeString":"2018-12-05",
        "stopTimeString":"2018-12-10",
        "submitOrSave":2,
        "actLevel":"10221001",
        "actLevelName":"A"
    },
    "actDealerList":[
        {
            "dealerCode":"CV0304"
        }
    ],
    "fileInfoDto":{
        "fileName":"暴风截图2018826656910656.jpg",
        "fileDiskName":"暴风截图2018826656910656.jpg",
        "fileType":10171001,
        "filePath":"amp_dev/8451a9321af64eb58c308d1290958ffb.jpg",
        "fileSuffix":"jpg",
        "fileSize":"50",
        "fileSizeUnit":"KB"
    }
}

r  = requests.post(url ,headers =headers ,json= body,verify=False)

result = r.json()
print(result)