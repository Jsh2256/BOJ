import sys
input = sys.stdin.readline
"""
1. 왼쪽 위가 w일경우
바뀌면 check표시
이중 for문으로 check 개수 표시
	중복으로 표시
	1 2 3 ...
	0번째~8번째
	1번째~9번째
	      ...
	
2. 왼쪽 위가 b일 경우

제일 먼저 해야 될 것
1. w로 시작할때 바꾼 개수 총
"""


n, m = map(int, input().split())
totalsum = []
board = []

for i in range(n):
    board.append(list(map(str, input().split())))

for i in range(n):
    for j in range(m):
        if board[i][j] == 'W':


print(board)
