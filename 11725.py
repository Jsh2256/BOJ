import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())
stack = []

graph = [[] for i in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph, start):
    visited = set([])
    q = deque([start])
    root = [[] for _ in range(n+1)]
    
    while q:
        cur_node = q.popleft()
        
        for next_node in graph[cur_node]:
            if next_node not in visited:
                visited.add(next_node)
                q.append(next_node)
                root[next_node] = cur_node
    return root

root = bfs(graph, 1)

for i in range(2, len(root)):
    print(root[i])