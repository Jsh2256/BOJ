import sys
input = sys.stdin.readline

n = int(input())

listA = []
f = []
for i in range(n):
    line = []
    for j in range(i+1):
        line.append(0)
    f.append(line)
for i in range(n):
    a = list(map(int, input().split()))
    listA.append(a)
    
g = [0]*n
f[0][0] = listA[0][0]

for x in range(1, n): # 층
    for i in range(x+1):
        if i == 0:
            f[x][0] = f[x-1][0] + listA[x][0]
        elif i == x:
            f[x][x] = f[x-1][x-1] + listA[x][x]
        else:
            f[x][i] = max(f[x-1][i-1], f[x-1][i])+listA[x][i]
    g[x] = max(f[x])
if n == 1:
    print(listA[0][0])
else:
    print(g[-1])

