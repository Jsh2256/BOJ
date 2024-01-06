import sys
input = sys.stdin.readline

a = list(map(str, input().rstrip()))
b = list(map(str, input().rstrip()))

dp = [0] * 1000001
l = 0
if len(a) > len(b):
    l = len(b)
else:
    l = len(a)
for i in range(l):
    for j in range(i+1):
        if b[j] in a:
            dp[i] = max(dp[i], dp[j]+1)
dp.sort()
print(dp[-1])