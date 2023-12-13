import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start, end, graph):
    q = deque([start])
    visited = set([start])
    dist = {start : 0}

    while q:
        cur = q.popleft()

        if cur == end:
            return dist[cur]
        for next in graph[cur]:
            if next not in visited:
                visited.add(next)
                q.append(next)
                dist[next] = dist[cur] + 1
    return -1
listDist = []
for i in range(1,n+1):
    total=0
    for j in range(1, n+1):
        total+=bfs(i,j,graph)
    listDist.append(total)
min = min(listDist)
for i in range(len(listDist)):
    if listDist[i] == min:
        print(i+1)
        break