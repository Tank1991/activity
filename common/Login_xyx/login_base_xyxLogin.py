#coding:utf-8
import requests

url = "https://test34.maxuscloud.cn/web/authcenter/index.html#/"

h = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    "Content-Type":"application/x-www-form-urlencoded"
}

body = {
    "loginAccount" : "18458333065",
    "loginPassword" : "aad7bc4a348ae43c1248ef27d342c050",
    "checkCode" : "5tir",
    "state" : "3da90911b704a6bad71ea68f8bc5d4bb"
}


r = requests.post(url,data = body,headers = h)
print(r.text)

