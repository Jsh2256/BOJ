import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    line = list(map(int, input().split()))
    graph.append(line)
for a in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    x1-=1
    y1-=1
    x2-=1
    y2-=1
    f = [0] * (1024)
    for x in range(x1,x2+1):
        g = [0] * (1024)
        for y in range(y1, y2+1):
            g[y] = g[y-1] + graph[x][y]
        f[x] = f[x-1] + g[y2]
    print(f[x2])