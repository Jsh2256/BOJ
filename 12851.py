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
            continue
        if v-1 >=0:
            if not visited[v-1] or dist[v-1] == dist[v] + 1:
                visited[v-1]=True
                q.append(v-1)
                dist[v-1] = dist[v]+1
        if v+1 <100001:
            if not visited[v+1] or dist[v+1] == dist[v] + 1:
                visited[v+1]=True    
                q.append(v+1)
                dist[v+1] = dist[v]+1 
        if  2*v < 100001:
            if not visited[2*v] or dist[2*v] == dist[v] + 1:
                visited[2*v]=True
                q.append(2*v)
                dist[2*v] = dist[v]+1 
    return listA
cnt=0
visited =[False] * (100001)
listA = bfs(n, k, visited)
listA.sort()
min = listA[0]
for target in listA:
    if target == min:
        cnt+=1
print(min)
print(cnt)