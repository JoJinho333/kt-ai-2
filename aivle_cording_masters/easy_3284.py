# 3284 해결
a = int(input())
b = [input() for _ in range(a)]
c = [0]
d = list(range(1,a+1))
for i in range(len(b)):
    if b[i] == 'D':
        c.insert(0, d[i])
    else:
        c.append(d[i])
for i in c:
    print(i, end=' ')