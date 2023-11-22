import sys

input = sys.stdin.readline
n = int(input())
listA = []

for _ in range(n):
    listA.append(input().strip())
setA = set(listA)
listA = list(setA)

listA.sort()
listA.sort(key=len)

print(*listA, sep='\n')
