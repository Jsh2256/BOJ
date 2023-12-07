import sys
from collections import deque
input = sys.stdin.readline

graph = []
n, m = map(int, input().split())
#visited = [[False]*m for _ in range(n)]
for i in range(n):
    graph.append(list(map(int, input().split())))

def bfs(start_x, start_y, graph):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    q = deque([(start_x, start_y,0)])
    visited = set([(start_x,start_y)])
    graph[start_x][start_y] = 0
    while q:
        x, y, dist = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                if (nx, ny) not in visited:
                    if graph[nx][ny] == 1:
                        if dist == -1:
                            q.append((nx, ny, -1))
                            graph[nx][ny] = -1
                        else:
                            visited.add((nx, ny))
                            q.append((nx, ny, dist+1))
                            graph[nx][ny] = dist+1
                    elif graph[nx][ny] == 0:
                        visited.add((nx, ny))
                        q.append((nx, ny, -1))
                        graph[nx][ny] = 0
                    
                    if graph[nx][ny] == -1:
                        if graph[x][y] >= 1:
                            if dist != -1:
                                visited.add((nx, ny))
                                q.append((nx, ny, dist+1))
                                graph[nx][ny] = dist+1
      
    return graph
                    
start_x = 0
start_y = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            start_x = i
            start_y = j
            
listD = bfs(start_x, start_y,graph)

for i in listD:
    for j in i:
        print(j, end=' ')
    print()


