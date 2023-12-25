import sys
input = sys.stdin.readline


n = int(input().strip())

while n > 4:
    n -= 4

if n == 1 or n == 3:
    print("SK")
else:
    print("CY")
