# 4300 펀드 해결

fund, cred = map(int, input().split())
m, n = map(int, input().split())

product = []
total = 0
for i in range(m):    
    product.append(int(input()))
    
product = sorted(product, reverse=True)

for i in range(n):
    total += product[i]

print(fund+(cred*total))