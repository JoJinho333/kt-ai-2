# 4295 배열 돌리기 해결

n = int(input())
a = list(map(int, input().split()))
print(" ".join(str(item) for item in a))
for i in range(n-1):
    a.append(a[0])
    del a[0]
    a = a
    print(" ".join(str(item) for item in a))