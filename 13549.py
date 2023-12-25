import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

def bfs(n,k,visited):
    visited[n] = True
    listA = []
    q = deque([n])
    dist = {n : 0}        
    while q:
        v = q.popleft()
        if v == k:
            listA.append(dist[v])
        if 2*v < 100001 and not visited[2*v]:
            q.append(2*v)
            visited[2*v]=True
            dist[2*v] = dist[v]    
        if v-1 >=0 and not visited[v-1]:
            visited[v-1]=True
            q.append(v-1)
            dist[v-1] = dist[v]+1
        if v+1 <100001 and not visited[v+1]:
            visited[v+1]=True
            q.append(v+1)
            dist[v+1] = dist[v]+1 
        
    return listA

visited =[False] * (100001)
listA = bfs(n, k, visited)
listA.sort()
print(listA[0])