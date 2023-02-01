# 3300
a = int(input())
list = []
list2 =[]
for i in range(6):
    n = (2**(2**i))+1
    list.append(n)
    
for i in range(1,10):
    b = list * 4*i
    list2.append(b)
    
for i in range(len(list2)):
    if list2[i] % a == 0:
        print("YES")
    else:
        print("NO")