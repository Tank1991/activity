import requests
import urllib3
urllib3.disable_warnings()

url = "https://test34.maxuscloud.cn/ampService/tSourceWebController/querySourceListByPid"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
    "xyx_jwt":"eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxMDAwMDAwMDAwNTY5MSIsIm1heHVzVXNlcklkIjoxMzQ3MTUwLCJ1c2VyT3JnTmFtZSI6Iue7temYs-W7uuWbveaxvei9pumUgOWUruacjeWKoeaciemZkOWFrOWPuCIsInVzZXJOYW1lIjoi5bSU5rW35rSLIiwidXNlcklkIjoxMDAwMDAwMDAwNTY5MSwicHJldmlvdXNVc2VySWQiOm51bGwsInVzZXJPcmdJZCI6MTAwMjE5MzEsIm1heHVzUHJldmlvdXNVc2VySWQiOm51bGwsInVzZXJQb3NpdGlvbiI6IjEwMDgxMDA4IiwiaXNNb2JpbGUiOjAsInByZXZpb3VzVXNlck5hbWUiOm51bGwsInByZXZpb3VzVXNlck9yZ0lkIjpudWxsLCJwcmV2aW91c1VzZXJQb3NpdGlvbiI6bnVsbCwiZXhwIjoxNTQyNzIxMjUyLCJjbGFzcyI6ImNvbS5zbWN2Lnh5eC5hcGkuYXV0aC5lbnRpdHkuYmFzZS5Kd3RVc2VyQ2xhaW1zIiwiaWF0IjoxNTQyNjM0ODUyLCJqdGkiOiJ4eXhKd3QiLCJwcmV2aW91c1VzZXJPcmdOYW1lIjpudWxsfQ.cV-J5jKCHZcnQqjMGWBBUq9D-rRbhl1Mx1CBvgHfxTTAbRErp3wf1rRPxaRuPnfxZ3xCU6cQK-K-nAz2gvlv3lMaesKLg4b5ZAINmB57OoHo5w9wKJrYhiWPy7CE3_CC_ucmf3UctwVnWUWuCu2ox_WKJu68f42Y807dAftxhZY",
    "SESSION":"dc96f92c-bd21-4bcf-a883-117da4f2b5f7"
}

r = requests.post(url ,headers =headers ,verify=False)

result = r.text

print(result)










