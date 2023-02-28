# 4307 반품 해결
n, money = map(int, input().split())

product = []
count = 0
for i in range(n):    
    product.append(int(input()))
    
product = sorted(product, reverse=True)

for i in range(n):    
    if money >= product[i]:
        money -= product[i]
        count+=1
        
print(count)