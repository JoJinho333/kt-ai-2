# 3285 해결
n = int(input())
a = list(map(int, input().split()))
p = [list(map(int, input().split())) for _ in range(n)]
price = []
for i in range(n):
    m = (abs(a[0]-p[i][0]) + abs(a[1]-p[i][1]))
    price.append(m)
print(min(price)*100)