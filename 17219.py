import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dicA = {}

for i in range(n+m):
    if i < n:
        a, b = map(str, input().split())
        dicA[a] = b
    else:
        site = input().rstrip()
        if site in dicA:
            print(dicA.get(site))