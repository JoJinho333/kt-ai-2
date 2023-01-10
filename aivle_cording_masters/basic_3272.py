# 3272 해결
n = input()
a = 0
for i in n:
    if i == '3':
        print("clap", end ='')
        a+=1
    if i == '6':
        print("clap", end ='')
        a+=1
    if i == '9':
        print("clap", end ='')
        a+=1
if a == 0:
    print(n)