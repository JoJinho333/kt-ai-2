# 3346 해결
import itertools

a = input()
b = list(map(''.join, itertools.permutations(a)))
list2 = []
print(b)
for i in range(len(b)):
    if int(b[i]) % 13 == 0:
        list2.append(1)
    else:
        list2.append(0)
        
if 1 in list2:
    print("YES")
else:
    print("NO")