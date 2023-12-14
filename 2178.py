import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []

for i in range(n):
    line = list(map(int, input().strip()))
    graph.append(line)

def bfs(start_x, start_y, end_x, end_y, graph):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    q = deque([(start_x, start_y, 1)])
    visited = set([(start_x, start_y)])

    while q:
        x,y,dist = q.popleft()
        if x == end_x and y == end_y:
            return dist
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                if (nx, ny) not in visited:
                    if graph[nx][ny] == 1:
                        q.append((nx, ny, dist+1))
                        visited.add((nx, ny))
    return -1         


print(bfs(0,0,n-1,m-1,graph))
