import requests
import urllib3
urllib3.disable_warnings()
#新增车展活动

url = "https://test102.maxuscloud.cn/ampService/actCarExhInfoWebController/saveOrUpdateCarExhDraftAct"


headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
    "xyx_jwt":"eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxMzQ2NDY2IiwiY2xhaW1zVHlwZSI6MSwibWF4dXNVc2VySWQiOjEzNDY0NjYsIm9wZW5JZCI6bnVsbCwid2VjaGF0TG9naW5PcGVuSWQiOm51bGwsInVzZXJOYW1lIjoi55So5oi3MDkyNlo2TmhFczAyIiwiZXhwIjoxNTQ0NDQ3NTEyLCJjbGFzcyI6ImNvbS5zbWN2Lm1heHVzLmF1dGguZW50aXR5Lkp3dFVzZXJDbGFpbXMiLCJ1dWlkIjoiNjc0YWJhNDM0NjlkNDZiOTk5MmUwYzFlMDk1NzM3OTAiLCJpYXQiOjE1NDM4NDI3MTIsImp0aSI6IjdlMDNkOTMwLWM0YTctNGExZi05ZDg1LTM3YWM2ZDg2NjNmOCJ9.Ht1wAESf-xiVdWdS55hr6Q8S3Mp1kZG6THjJ4HHX_O1hXNobeBs8QG3HgkZXKdV0jT_RhFgZa8-ElEDzEs8CnoumcHNVbzNQhzDIO6bvMUOJs_PoXx9dO-md_NZoly3umgw1MXzVNRyLsqdxViTfBjiC2D9aFKTfhgTNWMfZnw8; xyx_jwt=eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxMDAwMDAwMDAwNTUyMSIsIm1heHVzVXNlcklkIjoxMzQ2NDY2LCJ1c2VyT3JnTmFtZSI6IuS4iuaxveWkp-mAmiIsInVzZXJOYW1lIjoiY2h5IiwidXNlcklkIjoxMDAwMDAwMDAwNTUyMSwicHJldmlvdXNVc2VySWQiOm51bGwsInVzZXJPcmdJZCI6MTAwMDAwMDEsIm1heHVzUHJldmlvdXNVc2VySWQiOm51bGwsInVzZXJQb3NpdGlvbiI6IjEwMDgxMDIxIiwiaXNNb2JpbGUiOjAsInByZXZpb3VzVXNlck5hbWUiOm51bGwsInByZXZpb3VzVXNlck9yZ0lkIjpudWxsLCJwcmV2aW91c1VzZXJQb3NpdGlvbiI6bnVsbCwiZXhwIjoxNTQ0NDQ3NTEyLCJjbGFzcyI6ImNvbS5zbWN2Lm1heHVzLmF1dGguZW50aXR5Llh5eEp3dFVzZXJDbGFpbXMiLCJpYXQiOjE1NDM4NDI3MTIsImp0aSI6ImNiMzYzZTFjLTYzZDMtNDAyOC1iOGJhLWIxMDRhNGZjZDRlYiIsInByZXZpb3VzVXNlck9yZ05hbWUiOm51bGx9.YSHfskR-UXvZzfiyj8kJZWf1NSBdtEsXwLCsmX0FA0lB9GvnpitUEzBf9ADUJlo8_b7hGSvKsIfM5El6dGAN0a51cKGrwuHpj3bPxs2746i227Asv248PmpE3xDwdWidgozRc9ELxX7-ZNvjt2bHIsRD8Y7_jxVGg3ZpQLp5pA0",
    "Content-Type":"application/json;charset=UTF-8",
    "UserJwtToken":"eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxMzQ2NDY2IiwiY2xhaW1zVHlwZSI6MSwibWF4dXNVc2VySWQiOjEzNDY0NjYsIm9wZW5JZCI6bnVsbCwid2VjaGF0TG9naW5PcGVuSWQiOm51bGwsInVzZXJOYW1lIjoi55So5oi3MDkyNlo2TmhFczAyIiwiZXhwIjoxNTQ0NDQ3NTEyLCJjbGFzcyI6ImNvbS5zbWN2Lm1heHVzLmF1dGguZW50aXR5Lkp3dFVzZXJDbGFpbXMiLCJ1dWlkIjoiNjc0YWJhNDM0NjlkNDZiOTk5MmUwYzFlMDk1NzM3OTAiLCJpYXQiOjE1NDM4NDI3MTIsImp0aSI6IjdlMDNkOTMwLWM0YTctNGExZi05ZDg1LTM3YWM2ZDg2NjNmOCJ9.Ht1wAESf-xiVdWdS55hr6Q8S3Mp1kZG6THjJ4HHX_O1hXNobeBs8QG3HgkZXKdV0jT_RhFgZa8-ElEDzEs8CnoumcHNVbzNQhzDIO6bvMUOJs_PoXx9dO-md_NZoly3umgw1MXzVNRyLsqdxViTfBjiC2D9aFKTfhgTNWMfZnw8"
}

body = {"activityDto":{"id":"","activityName":"测试1","activityType":10141002,"activityMode":"T60,RV80B,MV80,EV80,G10,V80","firstSource":10000000000004,"secondSource":10000000000442,"content":"测试活动简述","beginTimeString":"2018-12-01","endTimeString":"2018-12-02","stopTimeString":"2018-12-03","submitOrSave":2,"actLevel":"10221001","actLevelName":"A"},"actDealerList":[{"dealerCode":"DV2802"}],"fileInfoDto":{"fileName":"SRS_知乎2.0--0514(1).docx","fileDiskName":"SRS_知乎2.0--0514(1).docx","fileType":10171003,"filePath":"amp_dev/8e17a4340c974b238564d033493194a4.docx","fileSuffix":"docx","fileSize":"112","fileSizeUnit":"KB"}}

aa= requests.post(url ,headers =headers ,json= body,verify=False)

