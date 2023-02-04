# 3312
a = int(input())
b = list(map(int,input().split()))
b.remove(max(b))
b.remove(max(b))
print(max(b))