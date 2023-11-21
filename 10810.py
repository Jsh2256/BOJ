import sys
input = sys.stdin.readline

n, m = map(int, input().split())
listA = []

listA = [0 for i in range(n)]

for a in range(m):
    i,j,k = map(int, input().split())
    for x in range(i,j+1):
        listA[x-1] = k

print(*listA)
