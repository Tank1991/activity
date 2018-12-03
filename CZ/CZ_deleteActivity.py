import requests
import urllib3
urllib3.disable_warnings()
#删除活动,传活动的ID

url = "https://test102.maxuscloud.cn/ampService/activityWebController/deleteActivity"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
    "xyx_jwt":"eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxMDAwMDAwMDAwNTUyMSIsIm1heHVzVXNlcklkIjoxMzQ2NDY2LCJ1c2VyT3JnTmFtZSI6IuS4iuaxveWkp-mAmiIsInVzZXJOYW1lIjoiY2h5IiwidXNlcklkIjoxMDAwMDAwMDAwNTUyMSwicHJldmlvdXNVc2VySWQiOm51bGwsInVzZXJPcmdJZCI6MTAwMDAwMDEsIm1heHVzUHJldmlvdXNVc2VySWQiOm51bGwsInVzZXJQb3NpdGlvbiI6IjEwMDgxMDIxIiwiaXNNb2JpbGUiOjAsInByZXZpb3VzVXNlck5hbWUiOm51bGwsInByZXZpb3VzVXNlck9yZ0lkIjpudWxsLCJwcmV2aW91c1VzZXJQb3NpdGlvbiI6bnVsbCwiZXhwIjoxNTQ0NDQ3NTEyLCJjbGFzcyI6ImNvbS5zbWN2Lm1heHVzLmF1dGguZW50aXR5Llh5eEp3dFVzZXJDbGFpbXMiLCJpYXQiOjE1NDM4NDI3MTIsImp0aSI6ImNiMzYzZTFjLTYzZDMtNDAyOC1iOGJhLWIxMDRhNGZjZDRlYiIsInByZXZpb3VzVXNlck9yZ05hbWUiOm51bGx9.YSHfskR-UXvZzfiyj8kJZWf1NSBdtEsXwLCsmX0FA0lB9GvnpitUEzBf9ADUJlo8_b7hGSvKsIfM5El6dGAN0a51cKGrwuHpj3bPxs2746i227Asv248PmpE3xDwdWidgozRc9ELxX7-ZNvjt2bHIsRD8Y7_jxVGg3ZpQLp5pA0",
    "Content-Type":"application/x-www-form-urlencoded"
}
body ={
    "activityId":"10000000032237"
}

r = requests.post(url,headers = headers,data = body,verify = False)

result = r.text
print(result)