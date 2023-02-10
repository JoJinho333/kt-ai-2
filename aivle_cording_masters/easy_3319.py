# 3319. 분수를 소수로 해결
from decimal import Decimal, getcontext
a, b = map(float,input().split())
c=int(input())

getcontext().prec=c
x=Decimal(a)/Decimal(b)
x=str(x)
result = x.ljust(c,"0")
com = len(result)-2

if int(c) == com:
    print(result)
else:
    print(result + '0'*(c-com), end = '')