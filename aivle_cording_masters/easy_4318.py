# 4318 전투력

n=int(input())
a=list(map(int,input().split()))
a = sorted(a)
man=0

for i in range(len(a)):
    if man < (a[i]*(len(a)-i)):
        man = (a[i]*(len(a)-i))

print(man)