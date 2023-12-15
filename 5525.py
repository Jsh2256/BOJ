import sys
input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())
s = input().strip()

def check():
    global state, start
    cnt = 0
    while start < m:
        if s[start] == 'I':
            if state == 0:
                state = 1
                return cnt

            elif state == 1:
                cnt += 1
                state = 0
                start+=1
        elif s[start] == 'O': #s[i] == 'O'
            if state == 0:
                state = 1
                start+=1
            elif state == 1:
                start+=1
                return cnt
    return cnt
ans = 0
state = 1
start = 0
while start < m:
    cnt = check()
    if cnt - n >= 0:
        ans+=cnt-n
print(ans)