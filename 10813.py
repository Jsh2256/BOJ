import sys
input = sys.stdin.readline

n, m = map(int, input().split())
listA = []

for x in range(n):
    listA.append(x+1)

for a in range(m):
    i,j = map(int, input().split())
    
    empty = listA[i-1]
    listA[i-1] = listA[j-1]
    listA[j-1] = empty

print(*listA)