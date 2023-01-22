#3281 해결
n, k = map(int, input().split())
l = list(map(int, input().split()))

ad = 0
result = []

for i in range(n-k+1):
    if 0 in l[i:i+k]:
        continue
        
    else:
        ad = sum(l[i:i+k])
    result.append(ad)
    
print(max(result))