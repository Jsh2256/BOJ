import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

def mt(a, b, c):
    if b == 0:
        return 1
    temp = mt(a, b//2, c)
    temp = (temp * temp) % c
    if b % 2 == 0:
        return temp
    else:
        return (temp*a)%c


print(mt(a, b, c))