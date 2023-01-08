# 3270 해결
a, b = map(int, input().split())
c, d = map(int, input().split())
if a + b <= c + d and a <= c and b <= (c + d -a):
    print("YES")
else:
    print("NO")