# 3349 해결
number = int(input())
x,y = map(int, input().split())

result = 0
minimum = ((result**2 + number**2 )**(0.5))/10 + (((result-x)**2+y**2)**(0.5)) / 5

for i in range(-100, 101):
    if ((i**2 + number **2)**(0.5))/10 + (((i-x)**2+y**2)**(0.5))/ 5 < minimum:
        result =i
        minimum = ((i**2 + number **2)**(0.5))/10 + (((i-x)**2+y**2)**(0.5))/ 5
        
print(result)