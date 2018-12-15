# coding:utf-8

li = [1, 3, 10, 9, 21, 35, 4, 6]

for j in range(len(li)-1):
    if li[j] > li[j+1]:
        li[j] , li[j+1] = li[j+1] , li[j]
        # print(li)
print(li)

# li.sort()
# print(li)

# 取字符串中的奇数项
a = "axbyczdj"
c = []
for i in range(len(a)):
    if i % 2 == 0:
        c.append(a[i])
print("".join(c))






