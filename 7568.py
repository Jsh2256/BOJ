import sys
input = sys.stdin.readline

n = int(input().strip())
dungchi = []
for i in range(n):
    x, y = map(int, input().split())
    dungchi.append([x, y, 0])


for i in range(n):
    num = 1
    for j in range(n):
        if j == i:
            continue
        if dungchi[i][0] < dungchi[j][0]:
            if dungchi[i][1] < dungchi[j][1]:
                num+=1
    dungchi[i][2] = num            
        
for i in dungchi:
    print(i[2], end=' ')