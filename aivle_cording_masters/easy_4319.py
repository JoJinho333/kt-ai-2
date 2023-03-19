# 4319
from collections import Counter
n = int(input())
list = []
for i in range(n):
    list.append(int(input()))
    list = sorted(list, reverse=True)
print(Counter(list).most_common(1)[0][0])