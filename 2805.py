import sys
input = sys.stdin.readline

n, m = map(int, input().split())

listA = list(map(int, input().split()))
    
start = 1
end = max(listA)


while start<=end:
    total = 0
    mid = (start+end)//2
    for i in listA:
        if i >= mid:
            total+=i-mid
    if total >= m:
        start = mid+1
    else:
        end = mid-1
    
print(end)