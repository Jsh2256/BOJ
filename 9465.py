import sys
input = sys.stdin.readline

t = int(input().strip())



for i in range(t):
    graph = []
    n = int(input().strip())
    for j in range(2):
        line = list(map(int, input().split()))
        graph.append(line)

    f = [0] * 100001
    u = [0] * 100001
    d = [0] * 100001
    if n == 1:
        u[0] = graph[0][0]
        d[0] = graph[1][0]
        f[0] = max(u[0],d[0])
        print(f[0])
    else:
        u[0] = graph[0][0]
        d[0] = graph[1][0]
        u[1] = d[0] + graph[0][1]
        d[1] = u[0] + graph[1][1]
        f[0] = max(u[0],d[0])
        f[1] = max(u[1],d[1])
        for x in range(2, n):
            u[x] = max(d[x-1], f[x-2])+ graph[0][x]
            d[x] = max(u[x-1], f[x-2]) + graph[1][x]
            f[x] = max(u[x],d[x])
        print(f[n-1])