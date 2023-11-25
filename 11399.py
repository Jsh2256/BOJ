import sys

input = sys.stdin.readline

n = int(input())
listA = []


listA = list(map(int, input().split()))

listA.sort()
sum = 0
for i in range(len(listA)):
    for j in range(i+1):
        sum+=listA[j]

print(sum)