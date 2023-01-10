a = int(input())

while True:
    print(int(a), end =' ')
    if a % 2 == 0:
        a = a/2
        if a == 1:
            print(int(a), end =' ')
            break
    else:
        a = 3*a+1
        if a == 1:
            print(int(a))
            break