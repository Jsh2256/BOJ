import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)

if n == 1:
    dp[1] = 1
    print(dp[1]%10007)
elif n == 2:
    dp[2] = 2
    print(dp[2]%10007)
elif n == 3:
    dp[3] = 3
    print(dp[3]%10007)
else:
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    
    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[i]%10007)