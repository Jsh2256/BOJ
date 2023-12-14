import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())

graph = []
visited = set([])
for i in range(n):
    line = list(map(int, input().strip()))
    graph.append(line)

def bfs(start_x, start_y, graph, visited):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    q = deque([(start_x, start_y)])
    visited.add((start_x, start_y))
    cnt = 1
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                if (nx, ny) not in visited:
                    if graph[nx][ny] == 1:
                        q.append((nx, ny))
                        visited.add((nx, ny))
                        cnt+=1
    return cnt
danji = 0
listtotal = []
for i in range(n):
    for j in range(n):
        if (i, j) not in visited:
            if graph[i][j] == 1:
                total = bfs(i, j, graph, visited)
                listtotal.append(total)
                danji += 1
listtotal.sort()

print(danji)
for i in listtotal:
    print(i)

