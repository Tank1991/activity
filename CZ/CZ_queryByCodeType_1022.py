import requests
import urllib3
urllib3.disable_warnings()
#活动的等级查询
url = "https://test102.maxuscloud.cn/ampService/tFixCodeWebController/queryByCodeType"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
    "xyx_jwt":"eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxMDAwMDAwMDAwNTUyMSIsIm1heHVzVXNlcklkIjoxMzQ2NDY2LCJ1c2VyT3JnTmFtZSI6IuS4iuaxveWkp-mAmiIsInVzZXJOYW1lIjoiY2h5IiwidXNlcklkIjoxMDAwMDAwMDAwNTUyMSwicHJldmlvdXNVc2VySWQiOm51bGwsInVzZXJPcmdJZCI6MTAwMDAwMDEsIm1heHVzUHJldmlvdXNVc2VySWQiOm51bGwsInVzZXJQb3NpdGlvbiI6IjEwMDgxMDIxIiwiaXNNb2JpbGUiOjAsInByZXZpb3VzVXNlck5hbWUiOm51bGwsInByZXZpb3VzVXNlck9yZ0lkIjpudWxsLCJwcmV2aW91c1VzZXJQb3NpdGlvbiI6bnVsbCwiZXhwIjoxNTQ0MzMxNzc3LCJjbGFzcyI6ImNvbS5zbWN2Lm1heHVzLmF1dGguZW50aXR5Llh5eEp3dFVzZXJDbGFpbXMiLCJpYXQiOjE1NDM3MjY5NzcsImp0aSI6IjJlMDNmYWJhLWI2NmEtNDk4NS04MGIxLWM3YjM1MWUxYTgwYSIsInByZXZpb3VzVXNlck9yZ05hbWUiOm51bGx9.Fu00AVpawV2C5AjAC8lV-76jJeiwKKRZEcKcUYUJ775vh-n_MQljcojwCrFO6dsjLA4MHvlssM7fz2ikpwm84Q6YGknlGK0g2PhlQY5yV1n6VBMRxJMpWBiSev_TtisRMzudw0Z-Bg8asBASLx1O5p4XRzqQcmCn4tLBIJkMOXM",
    "Content-Type":"application/x-www-form-urlencoded"
}

body = {
   "codeType":"1022"
}

r = requests.post(url ,headers =headers ,data= body,verify=False)

result = r.json()
print(type(result))
print(result['data'][0]["codeName"])













