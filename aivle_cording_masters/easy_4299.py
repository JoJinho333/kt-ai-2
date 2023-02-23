# 4299 볼펜 숫자의 곱 해결

from itertools import permutations

n = int(input())
a = list(map(int, input().split()))
answers_two = []
answers_three = []
total = []

for i in permutations(a, 2):    
    answers_two.append(i)
    
for i in permutations(a, 3):
    answers_three.append(i)

for i in range(len(answers_two)):
    total.append(answers_two[i][0] * answers_two[i][1])
    
for i in range(len(answers_three)):
    total.append(answers_three[i][0] * answers_three[i][1] * answers_three[i][2])
    
print(max(total))