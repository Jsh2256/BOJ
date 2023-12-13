import sys
import heapq
input = sys.stdin.readline

n = int(input())
listA = []

for _ in range(n):
    x = int(input())
    if x > 0 and x % 1 == 0:
        heapq.heappush(listA, -x)
    elif x == 0:
        if len(listA) == 0:
            print(0)
        else:   
            print(-heapq.heappop(listA))