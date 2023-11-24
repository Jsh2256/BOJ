import sys

input = sys.stdin.readline
n, m = map(int, input().split())

dicPoke = {}


for i in range(1,n+1):
    x = input().rstrip()
    dicPoke[x] = i  # 이름 : 번호
    dicPoke[i] = x  # 번호 : 이름


for i in range(m):
    qus = input().rstrip()
    if qus.isdigit():
        print(dicPoke[int(qus)])
    else:
        print(dicPoke[qus])
