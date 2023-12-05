import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

graph=[[] for _ in range(2*k)]

def makeGraph(graph,n, k):
    if n > 2*k or n < 0:
        return 0
    if not n in graph:
        if not n-1 in graph:
            if n-1 > 0:
                graph[n].append(n-1)
                graph[n-1].append(n)
                makeGraph(graph, n-1, k)
        if not n+1 in graph:
            graph[n].append(n+1)
            graph[n+1].append(n)
            makeGraph(graph, n+1, k)
        if not 2*n in graph:
            graph[n].append(2*n)
            graph[2*n].append(n)
            makeGraph(graph, 2*n, k)

makeGraph(graph, n, k)



def bfs(graph,n,k,visited):
    visited[n] = True
    q = deque([n])
    
    
    cnt=0
        
    while q:
        v = q.popleft()
        if v == k:
            print(cnt)
            break
        cnt+=1
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                q.append(i) 

visited =[False] * (2*k)
bfs(graph,n, k, visited)