import sys
input = sys.stdin.readline
cnt = 0
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)
count = 0
def dfs(node):
    
    visited[node] = True
    for a in graph[node]:
        if not visited[a]:
            dfs(a)
    

dfs(1)

for i in visited:
    if i == True:
        cnt+=1
print(cnt-1)