#coding:utf-8
from bs4 import BeautifulSoup
import requests
yo = open("yoyo.html","r")

soup = BeautifulSoup(yo, 'html.parser')
# print(soup.prettify())

tag = soup.title   #获取的是有title的标签
# print(tag)

tag2  = soup.p    #获取的是第一个标签的内容
# print(tag2)

#获取P标签里面的b标签内容
# print(tag2.b)

#获取标签里面的文字信息
# print(tag.string)

#获取a标签对象
a = soup.a
# print(a)
#将对象的属性打印成字典格式
att = a.attrs
#打印出需要的属性
# print(att['href'])

#获取所有符合查找条件的标签名称 list
all = soup.find_all("a")
# for i in all:
#     print(i)

r1 = requests.get("https://www.qiushibaike.com/", verify=False)

soup = BeautifulSoup(r1.content, "html.parser")
# class跟python系统关键字冲突
all2 = soup.find_all(class_="content")  # class_="content"
for i in all2:
    print(i.span.get_text().replace("\n",""))  #获取当前节点子孙节点的文本信息
