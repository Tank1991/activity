import requests
import urllib3
urllib3.disable_warnings()
from common.Login_xyx.get_UserJwtToken import *
#车展编辑-提交按钮
token = Get_Token_jwt().get_token()
jwt = Get_Token_jwt().get_jwt()
agent = Get_Token_jwt().get_User_Agent()

url = "https://test34.maxuscloud.cn/ampService/actCarExhInfoWebController/updateActCarExhInfo"

headers = {
    "User-Agent":agent,
    "xyx_jwt":jwt,
    "Content-Type":"application/json;charset=UTF-8"
}

body = {
    "activityDto":{
        "id":10000000033297,
        "activityName":"测试的哈",
        "activityType":10141002,
        "activityMode":"RV80B,T60,MV80,EV80,G10,V80,EG10",
        "firstSource":10000000000002,
        "secondSource":10000000000006,
        "content":"接口的活动简述",
        "beginTimeString":"2018-12-01",
        "endTimeString":"2018-12-05",
        "stopTimeString":"2018-12-10",
        "actLevel":10221001,
        "submitOrSave":1
    },
    "actDealerList":[
        {
            "dealerCode":"CV0304"
        }
    ],
    "fileInfoDto":{
        "isDelete":10011001,
        "createDate":None,
        "createBy":None,
        "updateDate":None,
        "updateBy":None,
        "fileId":10000000004787,
        "businessType":10091001,
        "businessId":10000000033297,
        "businessField":10101001,
        "fileName":"暴风截图2018826656910656.jpg",
        "fileDiskName":"暴风截图2018826656910656.jpg",
        "fileType":10171001,
        "filePath":"amp_dev/8451a9321af64eb58c308d1290958ffb.jpg",
        "fileSuffix":"jpg",
        "fileSize":"50",
        "fileSizeUnit":"KB",
        "businessTypeName":"活动",
        "businessFieldName":"其他附件",
        "fileTypeName":"图片",
        "excludeBusinessFieldList":None,
        "fileUrl":"https://cdn3cdn.maxuscloud.com/xyx/amp_dev/8451a9321af64eb58c308d1290958ffb.jpg",
        "thumbFileUrl":"https://cdn3.maxuscloud.com/xyx/amp_dev/8451a9321af64eb58c308d1290958ffb_120x120.jpg",
        "tagNames":None,
        "id":None
    }
}

r = requests.post(url ,headers =headers ,json= body,verify=False)

result = r.json()
print(result)