# 3307
n = int(input())
arr=[['1']]
for x in range(n-1):
    bf=[]
    a=sorted(set(arr[x]))
    for y in list(a):
        bf.append(y)
        bf.append(str(arr[x].count(y)))
    arr.append(bf)
print("".join(arr[-1]))