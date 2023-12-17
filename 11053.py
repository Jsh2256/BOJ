import sys
input = sys.stdin.readline

n = int(input().strip())
listA = list(map(int, input().split()))

dp =[1]*n
#listA.reverse()
for i in range(1,n):
    for j in range(i):
        if listA[i] > listA[j]:
            dp[i] = max(dp[i], dp[j]+1)
        
dp.sort()
print(dp[-1])