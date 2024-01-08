import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
arr = []

while True:
    try:
        x = int(input())
        arr.append(x)
    except:
        break

def recursion(first, end):
    if first > end:
        return
    mid = end+1
    
    for i in range(first+1, end+1):
        if arr[first]<arr[i]:
            mid = i
            break
        

    recursion(first+1, mid-1)
    recursion(mid, end)
    print(arr[first])

recursion(0,len(arr)-1)
