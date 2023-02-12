# 3323 동네 한 바퀴
a, b = map(int, input().split())
w_list = []
n_list = []
for i in range(a):
    w,n = input().split()
    w_list.append(w)
    n_list.append(n)
r1 = set(w_list)
r2 = set(n_list)
if r1 == r2:
    print("YES")
else:
    print("NO")