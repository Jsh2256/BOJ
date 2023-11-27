import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)
sum=0
if n == 1:
    dp[1] = 1
    print(dp[n]%10007)

else:
    dp[1] = 1
    for i in range(2, n+1):
        if i%2==0:
            dp[i] = (2*dp[i-1])+1
        else:
            dp[i] = (2*dp[i-1])-1
    print(dp[n]%10007)