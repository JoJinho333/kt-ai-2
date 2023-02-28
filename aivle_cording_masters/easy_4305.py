# 4305 관광지 해결

n = int(input())
answer = 0
arr = []

for i in range(n):
    arr.append(list(input()))
    
def dfs(grap, start, visited):
    visited[start] = 1
    
    for i in range(n):
        if arr[start][i] == "Y":
            if visited[i] == 0:
                dfs(grap, i, visited)

for i in range(n):
    score = 0
    visited = [0] * n
    dfs(arr,i,visited)
    score = sum(visited) - 1
    
    if answer < score:
        answer = score
print(answer)