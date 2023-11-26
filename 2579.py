#import sys
#input = sys.stdin.readline

n = int(input())
listA = []
for _ in range(n):
    score = int(input())
    listA.append(score)
dp = [0]*n
if len(listA)<=2:
    print(sum(listA))

else:
    dp[0] = listA[0]
    dp[1] = listA[0] + listA[1]

    for i in range(2,n):
        dp[i] = max(dp[i-3]+listA[i]+listA[i-1],dp[i-2]+listA[i])
    print(dp[-1])