# 3318 친화수 해결

x, y = map(int,input().split())

sum1 = 0
sum2 = 0

for i in range(1, x):
    if (x % i) == 0:
        sum1 += i
for j in range(1, y):
    if (y % j) == 0:
        sum2 += j
        
if (sum1 == y) and (sum2 == x):
    print("YES")
else:
    print("NO")