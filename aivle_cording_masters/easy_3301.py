# 3301 예비군 해결
n, army, a, p = input().split()
n=int(n)
if p == 'Private':
    if n == 0:
        print(0)
    elif 1 <= n <= 4:
        if a == 'N':
            if army =='ROKAF':
                print(28)
            else:
                print(32)
        else:
            print(28)
    else:
        print(20)
else:
    if n == 0:
        print(0)
    else:
        print(28)