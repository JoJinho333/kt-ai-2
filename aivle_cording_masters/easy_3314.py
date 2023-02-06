# 3314 사탕 나누기 해결
n = int(input())
a = input().split()

b = []
c = []
m_list = []
s = 0
count = 0

for i in range(len(a)):
    b.append(int(a[i]))
    s += b[i]
m = int(s/len(b))

for i in range(n):
    m_list.append(m)

for i in range(len(b)):
    c.append(b[i]-m_list[i])

for i in range(len(c)):
    if c[i] > 0:
        count += c[i]

print(count)