# 3264 해결
a, b, c = map(int, input().split())

a = a*a
b = b*b*c
if b >= a:
    print("YES")
else:
    print("NO")