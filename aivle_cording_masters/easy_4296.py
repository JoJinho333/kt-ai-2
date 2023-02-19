# 4296 해결

a,b = map(float, input().split())

while True:
    print(format(a, '.2f' ), end=' ')
    a = a + 0.01

    if a >= b:
        break