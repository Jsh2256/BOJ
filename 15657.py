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
            if len(ans)>0:
                if max(ans)<=i:
                    ans.append(i)
                    back()
                    ans.pop()
            else:
                ans.append(i)
                back()
                ans.pop()
back()