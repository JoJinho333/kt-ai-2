# 3271 해결
n = int(input())
q = input().split()
s = 0
for i in range(n):
    s += int(q[i])
if s >= 100:
    print(0)
else:
    print(100 - s)