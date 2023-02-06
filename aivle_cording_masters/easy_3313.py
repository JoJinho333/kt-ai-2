# 3313 자동차 번호판 해결
a = input()
b = []
for i in range(len(a)):
    b.append(int(a[i]))
b.sort()
if int(b[0]) + int(b[3]) == int(b[1]) + int(b[2]):
    print("YES")
else:
    print("NO")