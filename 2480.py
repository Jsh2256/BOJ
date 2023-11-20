a,b,c = map(int, input().split())
prize = 0

if a == b and b == c:
    prize = 10000 + a * 1000

elif a == b:
    prize = 1000 +  a * 100
elif b == c:
    prize = 1000 +  b * 100
elif a == c:
    prize = 1000 +  a * 100

else:
    max = a
    if max < b:
        max = b
    if max < c:
        max = c
    prize = max * 100

print(prize)

