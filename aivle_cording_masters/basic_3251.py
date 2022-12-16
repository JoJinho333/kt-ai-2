# 3251 해결

a, b, c, d, e = map(int,input().split())
x = [a, b, c, d, e]
p = []
for i in range(5):
    if x[i] < 40:
        break
    else:
        if int(x[0]+x[1]+x[2]+x[3]+x[4])/5 >= 60:
            p.append(1)
if len(p) == 5:
    print("P")
else:
    print("F")