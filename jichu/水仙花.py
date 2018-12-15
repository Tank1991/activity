
sxh = []
for i in range(100, 1000):
    s = 0
    m = list(str(i))
    for j in m:
        s += int(j)**len(m)
    # print("".join(m),s)
    if i == s:
        print(i)
        sxh.append(i)

print("100-999的水仙花数：%s" % sxh)


a = [1, 3, 10, 9, 21, 35, 4, 6]

s = range(1, len(a))[::-1]
print(list(s))  # 交换次数

for i in s:
    for j in range(i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
    print("第 %s 轮交换后数据：%s" % (len(s)-i+1, a))
print(a)