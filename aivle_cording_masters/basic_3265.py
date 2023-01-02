# 3265 해결
a, b = map(int, input().split())
if b == 0:
    print(abs(60-a))
elif abs(a-b) > 30:
    print(abs(0 - a) + abs(60-b))
else:
    print(abs(a - b))