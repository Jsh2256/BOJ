a,b = map(int, input().split())
c = int(input())

b+=c

while True:
    if a < 24 and b < 60:
        print(a, b)
        break
    if b >= 60:
        a+=1
        b-=60
    if a >= 24:
        a -= 24