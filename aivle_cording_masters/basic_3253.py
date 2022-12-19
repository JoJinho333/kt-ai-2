# 3253 해결
a, b, c = map(int,input().split())
x = [a, b, c]
x.remove(max(x))
print(int((x[0]*x[1])/2))