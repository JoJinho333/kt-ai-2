# 4316
n = int(input())
list = []
for i in range(n):
    input_data = input().split()
    list.append((int(input_data[0]), input_data[1]))
    
list = sorted(list, key=lambda student: student[0],reverse=True)
for student in list:
    print(student[1])