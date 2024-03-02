import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    stack = []
    ps = list(map(str, input().strip()))
    for j in range(len(ps)):
        if len(stack) == 0:
            stack.append(ps[j])
        elif stack[-1] == ps[j]:
            stack.append(ps[j])
        else:
            if stack[0] != ')':
                stack.pop()
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")


