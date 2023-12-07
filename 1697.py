import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

def bfs(n,k,visited):
    visited[n] = True
    q = deque([n])
    dist = {n : 0}        
    while q:
        v = q.popleft()
        if v == k:
            print(dist[v])
            break
        if v-1 >=0 and not visited[v-1]:
            visited[v-1]=True
            q.append(v-1)
            dist[v-1] = dist[v]+1
        if v+1 <100001 and not visited[v+1]:
            visited[v+1]=True
            q.append(v+1)
            dist[v+1] = dist[v]+1 
        if  2*v < 100001 and not visited[2*v] :
            visited[2*v]=True
            q.append(2*v)
            dist[2*v] = dist[v]+1 
        

visited =[False] * (100001)
bfs(n, k, visited)
