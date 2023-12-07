import sys
input = sys.stdin.readline
from collections import deque

def bfs(graph, node, visited):
    queue = deque([node])
    visited[node] = True
    
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
    
    return cnt

n, m = map(int, input().split())
cnt=0
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, len(graph)):
    if visited[i]==False:
        bfs(graph, i, visited)
        cnt+=1
print(cnt)
