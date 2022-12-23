# 3255 (해결)
n, m = map(int, input().split())
a = [list(input().split()) for _ in range(n)]
b = [list(input().split()) for _ in range(n)]
c = [[0]*m for _ in range(n)]
d = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        d[i][j]=a[i][j]+b[i][j]
for k in range(n):
    for l in range(m):
        if d[k][l][0]==d[k][l][1]:
            c[k][l]=d[k][l][0]
        elif d[k][l]=='RG' or d[k][l]=='GR':
            c[k][l]='Y'
        elif d[k][l]=='GB' or d[k][l]=='BG':
            c[k][l]='C'
        else: c[k][l]='M'          
for x in c: 
    print(*x)