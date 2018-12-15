def digui(n):
    if n == 1:
        return 1
    else:
        return n*digui(n-1)
a = 10
print(digui(a))

from functools import reduce
# 方法1：推荐！
a = 10
b = reduce(lambda x, y: x*y, range(1, a+1))
print(b)

a = 0
b = 1
while b < 100:
    print(b, end=",")
    a, b = b, a+b