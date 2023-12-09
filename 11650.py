import sys
input = sys.stdin.readline

n = int(input())
listA=[]
for _ in range(n):
    x, y = map(int, input().split())
    listA.append([x, y])
listA.sort()
for i in listA:
    print(*i)