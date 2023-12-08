import sys
from collections import deque
input = sys.stdin.readline

graph = []
m, n = map(int, input().split())

for i in range(n):
    graph.append(list(map(int, input().split())))

def bfs(listStart, graph):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    q = deque([])
    visited = set([])
    for i in range(len(listStart)):
        q.append((listStart[i][0],listStart[i][1],0))
        visited.add((listStart[i][0],listStart[i][1]))
        graph[listStart[i][0]][listStart[i][1]] = 0
    while q:
        x, y, dist = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                if (nx, ny) not in visited:
                    if graph[nx][ny] == 0: # 0 갈 수 있는 루트
                        if dist == -2: # 갇혀있는 부분 -1로 바꿈
                            q.append((nx, ny, -2))
                            graph[nx][ny] = -2
                        else:   # 갇혀있는 부분이 아닌 곳 거리 증가
                            visited.add((nx, ny))
                            q.append((nx, ny, dist+1))
                            graph[nx][ny] = dist+1
                    elif graph[nx][ny] == -1: # -1 갈 수 없는 루트
                        visited.add((nx, ny))
                        q.append((nx, ny, -2))
                        graph[nx][ny] = 0
                    
                    if graph[nx][ny] == -2: # 갈 수 없는 곳인줄 알았지만
                        if graph[x][y] >= 0: # 연결되어 있음
                            if dist != -2:
                                visited.add((nx, ny))
                                q.append((nx, ny, dist+1))
                                graph[nx][ny] = dist+1
      
    return graph
                    
start_x = 0
start_y = 0
listStart = []
isone = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            start_x = i
            start_y = j
            listStart.append([i,j])
            isone+=1
            
listD = bfs(listStart,graph)
max = 0
cnt=0
for i in listD:
        for j in i:
            if j == -2:
                cnt+=1
            elif max < j:
                max = j
            
if cnt>0 or isone == 0:
    print(-1)
else:
    print(max)
        


