# 3291
m = list(map(int, input().split()))
h = []
last = 0
for i in range(len(m)):
    if m[i] == 1:
        h.append('L')
        last = ''
    elif m[i+1]