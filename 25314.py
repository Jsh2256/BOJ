import sys
input = sys.stdin.readline

n = int(input())

a = n//4
for i in range(a):
    print("long", end=" ")
print("int")