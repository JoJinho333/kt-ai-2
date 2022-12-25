# 3258 해결
# 1 가위 / 2 바위 / 3 보
# 1 > 3
# 1 < 2
# 2 < 3
a = int(input())
s1 = 0
s2 = 0

for i in range(a):
    b, c = map(int,input().split())
    
    if b == 1 and c == 3:
        s1+=1
        
    elif b == 1 and c == 2:
        s2+=1
    
    elif b == c:
        s1+=0
        s2+=0
        
    elif b == 2 and c == 1:
        s1 += 1
    
    elif b == 2 and c == 3:
        s2 += 1
        
    elif b == 3 and c == 1:
        s2 += 1
        
    elif b == 3 and c == 2:
        s1 += 1
        
print(s1, s2)