# 4313

import copy

n = int(input())
m = list(map(int, input().split()))
count = 0

m_list = copy.deepcopy(m)
m_list.append(0)

for i in range(n):
    if m_list[i] != m_list[i+1]:
        count+=1

if len(set(m)) == 1:
    print(1)
else: 
    print(count-1)