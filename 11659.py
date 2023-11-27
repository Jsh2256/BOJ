import sys
input = sys.stdin.readline

n, m = map(int, input().split())
listA = list(map(int, input().split()))
dp = [0] *(n+1)
for y in range(1, n+1):
    dp[y] = dp[y-1] + listA[y-1]
for x in range(m):
    i, j = map(int, input().split())
    print(dp[j]-dp[i-1])