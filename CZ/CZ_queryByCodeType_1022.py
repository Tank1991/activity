import requests
import urllib3
urllib3.disable_warnings()
url = "https://test102.maxuscloud.cn/ampService/tFixCodeWebController/queryByCodeType"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
    "xyx_jwt":"eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxMDAwMDAwMDAwNTUyMSIsIm1heHVzVXNlcklkIjoxMzQ2NDY2LCJ1c2VyT3JnTmFtZSI6IuWMl-S6rOaxh-mTluWkp-mAmuaxvei9pumUgOWUruacjeWKoeaciemZkOWFrOWPuCIsInVzZXJOYW1lIjoi5bSU5rW35rSLIiwidXNlcklkIjoxMDAwMDAwMDAwNTUyMSwicHJldmlvdXNVc2VySWQiOm51bGwsInVzZXJPcmdJZCI6MTAwMDcwMTcsIm1heHVzUHJldmlvdXNVc2VySWQiOm51bGwsInVzZXJQb3NpdGlvbiI6IjEwMDgxMDA4IiwiaXNNb2JpbGUiOjAsInByZXZpb3VzVXNlck5hbWUiOm51bGwsInByZXZpb3VzVXNlck9yZ0lkIjpudWxsLCJwcmV2aW91c1VzZXJQb3NpdGlvbiI6bnVsbCwiZXhwIjoxNTQ0MDE2MTg0LCJjbGFzcyI6ImNvbS5zbWN2Lm1heHVzLmF1dGguZW50aXR5Llh5eEp3dFVzZXJDbGFpbXMiLCJpYXQiOjE1NDM0MTEzODQsImp0aSI6IjQ5MDdhNWJiLWM0M2EtNGQ3MS04MmE1LTJmNWMyZDVhZDMxYiIsInByZXZpb3VzVXNlck9yZ05hbWUiOm51bGx9.L05rGtCNLgsp3UZcD4koXZvUo_wHMGd4jwo6WTLx3aVoa2ju1oKdPzS4u2ZwwvBOog1xlSOKELOTFjWFthUlTsf8hGH3dwgCH_1-lHaFiqjPcVZQSFa4DAOqqby8myXE042oTE5gSaBJdHNEdgGVExRbXY8WJQ9HFUlqthvMzAU",
    "SESSION":"dc96f92c-bd21-4bcf-a883-117da4f2b5f7"
}

body = {
    "codeType":"1022"   #1022
}

r = requests.post(url , data = body ,headers =headers ,verify=False)

result = r.content.decode("utf-8")

print(result)





















