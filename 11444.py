"""

not solve - time error

"""


import sys
input = sys.stdin.readline

n = int(input().strip())

f = [0] * 3

if n >= 2:
    f[0] = 0
    f[1] = 1
    f[2] = 1
    for x in range(3, n+1):
        f[x%3] = f[(x-1)%3] + f[(x-2)%3]
    print(f[n%3]%1000000007)
    
else:
    print(n%1000000007)