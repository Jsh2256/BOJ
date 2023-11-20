x = int(input())
n = int(input())
listPrice = []
for i in range(n):
    a, b = map(int, input().split())
    x -= a * b

if x == 0:
    print("Yes")

else :
    print("No")