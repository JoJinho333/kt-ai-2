# 3316 에어컨 해결
n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
b = [0]*50
c = []
for i in range(n):
    for j in range(2):
        c.append(a[i][j]-1)
        
for i in range(len(c)-1):        
    for j in range(c[i],c[i+1]+1,1):        
        b[j] += 1

for index, value in enumerate(b):
    if value == max(b):
        print(index+1)
        break