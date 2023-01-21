# 3280 해결
n = int(input())
word = []
num = []
for i in range(n):
    w,a = input().split()
    word.append(w)
    num.append(a)
    
w2 = input()
for i in range(n):
    if w2 == word[i]:
        print(num[i])
    elif w2 not in word:
        print(-1)
        break