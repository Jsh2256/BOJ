import sys
input = sys.stdin.readline

N = int(input())
listA = []
listA = list(map(int, input().split()))
listA.sort()
length = len(listA)

M = int(input())
listB = list(map(int, input().split()))

for i in range(M):
    target = listB[i]
    left = 0
    right = length-1
    middle = length//2
    isThere = False
    while left <= right:
        middle = (right + left)//2
        if listA[middle] == target:
            isThere = True
            break
        elif listA[middle] < target:
            left = middle + 1
        elif listA[middle] > target:
            right = middle - 1
            
    if isThere == True:
        print("1")
    else:
        print("0")
