import sys
from collections import deque
input = sys.stdin.readline


dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def IsValid(pos):
    if pos[0] < 0 or pos[0] >= n or pos[1] < 0 or pos[1] >= m:
        return False
    elif cabbage[pos[0]][pos[1]]==1:
        return True
    else:
        return False
def bfs(start):
    q = deque()
    q.append(start)

    while q:
        curpos = q.popleft()
        listPos.remove(curpos)
        cabbage[curpos[0]][curpos[1]]=0
        for i in range(4):
            nextpos = [curpos[0] + dy[i],curpos[1] + dx[i]]
            if IsValid(nextpos):
                if not nextpos in q:
                    q.append(nextpos)
t = int(input())
                 
for _ in range(t):
    m, n, k = map(int, input().split())
    cabbage = [[0 for j in range(m)] for i in range(n)]   
    count = 0
    listPos = []
    for _ in range(k):
        x, y = map(int, input().split())
        cabbage[y][x] = 1
        listPos.append([y,x])
    while listPos:
        for i in listPos:
            bfs(i)
            count+=1
    print(count)



    





