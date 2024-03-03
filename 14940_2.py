import sys
input = sys.stdin.readline
from collections import deque

graph = []
n, m = map(int, input().split())
ans = [[-1 for i in range(m)] for j in range(n)]

for _ in range(n):
    graph.append(list(map(int, input().split())))

def bfs(start_x, start_y, ans):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0 ,0]
   

    visited = set([(start_x, start_y)])
    queue = deque([(start_x, start_y, 0)])

    while queue:
        x, y, dist = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                if (nx, ny) not in visited:
                    if graph[nx][ny] == 1:
                        visited.add((nx, ny))
                        queue.append((nx, ny, dist + 1))
                        ans[nx][ny] = dist + 1
                    elif graph[nx][ny] == 0:
                        ans[nx][ny] = 0
x=0
y=0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            x = i
            y = j
        if graph[i][j] == 0:
            ans[i][j] = 0

bfs(x,y,ans)
ans[x][y] = 0
for i in ans:
    print(*i, sep=' ')