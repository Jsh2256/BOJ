import sys
input = sys.stdin.readline

n = int(input())
listA = []
countBlue=0
countwhite=0
for y in range(n):
    listA.append(list(map(int, input().split()))) 

def re(n,listA):
    global countwhite
    global countBlue
    cntB = 0
    cntW = 0
    for i in range(len(listA)):
        for j in range(len(listA)):
            if listA[i][j] == 1:
                cntB+=1
            else:
                cntW+=1
                
    if cntB == n*n:
        countBlue+=1
    elif cntW == n*n:
        countwhite+=1
    else:
        tmp = []
        for i in range(0, n//2):
            line = []
            for j in range(0, n//2):
                line.append(listA[i][j])
            tmp.append(line)
        re(n//2, tmp)
        tmp.clear()
        for i in range(0, n//2):
            line = []
            for j in range(n//2, n):
                line.append(listA[i][j])
            tmp.append(line)
        re(n//2, tmp)
        tmp.clear()
        for i in range(n//2, n):
            line = []
            for j in range(0, n//2):
                line.append(listA[i][j])
            tmp.append(line)
        re(n//2, tmp)
        tmp.clear()
        for i in range(n//2, n):
            line = []
            for j in range(n//2, n):
                line.append(listA[i][j])
            tmp.append(line)
        re(n//2, tmp)
        tmp.clear()
                
re(n,listA)
print(countwhite)
print(countBlue)

