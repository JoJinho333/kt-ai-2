#3282
n, k = map(int, input().split())
m = list(map(int, input().split()))

a = max(m)
m.remove(max(m))
b = max(m)
print(a + b)