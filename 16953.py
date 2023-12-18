import sys
from collections import deque
input = sys.stdin.readline
max = 1000000001
n, k = map(int, input().split())

def bfs(n,k):
    
    q = deque([n])
    dist = {n : 0}        
    while q:
        v = q.popleft()
        if v == k:
            return dist[v]
        if 0 <= int(str(v)+'1') <= k:
            q.append(int(str(v)+'1'))
            dist[int(str(v)+'1')] = dist[v]+1
        if  2*v <= k:
            q.append(2*v)
            dist[2*v] = dist[v]+1
    return -1
        

tmp = bfs(n, k)
if tmp == -1:
    print(-1)
else:
    print(tmp+1)