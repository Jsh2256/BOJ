import sys
input = sys.stdin.readline

n, m = map(int, input().split())
listA = list(map(int, input().split()))
listA.sort()
ans = []

def back():
    if len(ans) == m:
        print(" ".join(map(str, ans)))
        return 
    for i in listA:
        #if i not in ans:
            ans.append(i)
            back()
            ans.pop()
back()