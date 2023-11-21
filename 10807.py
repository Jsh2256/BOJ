import sys
input = sys.stdin.readline

n = int(input())
cnt=0
listA = list(map(int, input().split()))

target = int(input())

length = len(listA)

for i in range(length):
    if target == listA[i]:
        cnt += 1

print(cnt)