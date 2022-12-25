# 3257 해결
a = int(input())
b = 3
def solution(a,b):
    if a>b:
        max = a
    else:
        max = b
        
    for i in range(max,a*b+1):
        if i%a == 0 and i%b==0:
            answer = i
            break
    return answer

c = solution(a,b)
print(c)