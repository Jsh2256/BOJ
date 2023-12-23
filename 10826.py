import sys
input = sys.stdin.readline

n = int(input().rstrip())

f = [0] * (n+1)

if n >= 2:
    f[0] = 0
    f[1] = 1
    f[2] = 1
    for x in range(2, n+1):
        f[x] = f[x-1] + f[x-2]

    print(f[n])
else:
    print(n)