# 4302 레크리에이션 해결

n = int(input())
m = list(map(int, input().split()))
a,b = map(int, input().split())

print(min(m[a-1:b]))