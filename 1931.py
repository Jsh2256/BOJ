import sys
input = sys.stdin.readline

n = int(input())
listA = []
for _ in range(n):
    s, e = map(int, input().split())
    listA.append([s, e])

listA.sort(key=lambda x : (x[1], x[0]))

listB = [-1]
cnt=0
for i in listA:
    if i[0] >= listB[-1]:
        for j in range(i[0], i[1]+1):
            listB.append(j)
        cnt+=1
print(cnt)