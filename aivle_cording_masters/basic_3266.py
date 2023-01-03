# 3266 해결
n = int(input())
a = [input() for _ in range(n)]
b = []

for i in range(len(a)):
    b.append(int(a[i]))
    if b[i] % 2 == 0:
        print("R")
    else:
        print("L")