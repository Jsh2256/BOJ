import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for i in range(n):
    x = list(map(str, input().strip()))
    graph.append(x)

def bfs(start_x, start_y, graph):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    cnt = 0
    q = deque([(start_x, start_y)])
    visited = set([(start_x,start_y)])
    
    while q:
        x, y = q.popleft()
        if graph[x][y]=='P':
            cnt+=1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                if (nx, ny) not in visited:
                    if graph[nx][ny] == 'O':
                        visited.add((nx, ny))
                        q.append((nx, ny))
                        
                    elif graph[nx][ny] == 'X':
                        visited.add((nx, ny)) 
                    
                    elif graph[nx][ny] == 'P':
                        visited.add((nx, ny))
                        q.append((nx, ny))
    return cnt

start_x=0
start_y=0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'I':
            start_x = i
            start_y = j

if bfs(start_x,start_y,graph) == 0:
    print('TT')
else:
    print(bfs(start_x,start_y,graph))