# 3293
a = int(input())
b = input().split()
temp = 0
count = [0]*a

list = []
for i in range(len(b)):
    list.append(int(b[i]))
    
for i in range(a):
    for j in range(a-1):
        if list[j] > list[j+1]:
            temp = list[j]
            list[j] = list[j+1]
            list[j+1]=temp
            count.append(1)
print(count1)

print(list)