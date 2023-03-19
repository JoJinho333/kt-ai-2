# 4322 해결
n = int(input())
list = []
for i in range(n):
    input_data = input().split()
    list.append((input_data[0], int(input_data[1])))
    
list = sorted(list, key=lambda student: student[1])
for student in list:
    print(student[0], end = ' ')