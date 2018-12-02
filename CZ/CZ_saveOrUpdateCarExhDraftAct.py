import requests
import urllib3
urllib3.disable_warnings()
#新增车展活动

url = "https://test102.maxuscloud.cn/ampService/actCarExhInfoWebController/saveOrUpdateCarExhDraftAct"


headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
    "xyx_jwt":"eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxMDAwMDAwMDAwNTUyMSIsIm1heHVzVXNlcklkIjoxMzQ2NDY2LCJ1c2VyT3JnTmFtZSI6IuS4iuaxveWkp-mAmiIsInVzZXJOYW1lIjoiY2h5IiwidXNlcklkIjoxMDAwMDAwMDAwNTUyMSwicHJldmlvdXNVc2VySWQiOm51bGwsInVzZXJPcmdJZCI6MTAwMDAwMDEsIm1heHVzUHJldmlvdXNVc2VySWQiOm51bGwsInVzZXJQb3NpdGlvbiI6IjEwMDgxMDIxIiwiaXNNb2JpbGUiOjAsInByZXZpb3VzVXNlck5hbWUiOm51bGwsInByZXZpb3VzVXNlck9yZ0lkIjpudWxsLCJwcmV2aW91c1VzZXJQb3NpdGlvbiI6bnVsbCwiZXhwIjoxNTQ0MzMxNzc3LCJjbGFzcyI6ImNvbS5zbWN2Lm1heHVzLmF1dGguZW50aXR5Llh5eEp3dFVzZXJDbGFpbXMiLCJpYXQiOjE1NDM3MjY5NzcsImp0aSI6IjJlMDNmYWJhLWI2NmEtNDk4NS04MGIxLWM3YjM1MWUxYTgwYSIsInByZXZpb3VzVXNlck9yZ05hbWUiOm51bGx9.Fu00AVpawV2C5AjAC8lV-76jJeiwKKRZEcKcUYUJ775vh-n_MQljcojwCrFO6dsjLA4MHvlssM7fz2ikpwm84Q6YGknlGK0g2PhlQY5yV1n6VBMRxJMpWBiSev_TtisRMzudw0Z-Bg8asBASLx1O5p4XRzqQcmCn4tLBIJkMOXM",
    "Content-Type":"application/json;charset=UTF-8"
}

body = {"activityDto":
            {"id":"",
             "activityName":"接口测试",
             "activityType":10141002,
             "activityMode":"RV80B,T60,MV80",
             "firstSource":10000000000002,
             "secondSource":10000000000007,
             "content":"123活动简述",
             "beginTimeString":"2018-12-01",
             "endTimeString":"2018-12-02",
             "stopTimeString":"2018-12-05",
             "submitOrSave":2,
             "actLevel":"10221001",
             "actLevelName":"A"},
        "actDealerList":
            [{"dealerCode":"JXS004"}],
        "fileInfoDto"
            :{"fileName":"活动接口.xlsx",
              "fileDiskName":"活动接口.xlsx",
              "fileType":10171003,
              "filePath":"amp_dev/956dee485f334d1d83614e6444e6da5d.xlsx",
              "fileSuffix":"xlsx",
              "fileSize":"9",
              "fileSizeUnit":"KB"}
        }

r = requests.post(url ,headers =headers ,json= body,verify=False)

result = r.json()
print(result)