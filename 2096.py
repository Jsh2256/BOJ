import sys
input = sys.stdin.readline

n = int(input().rstrip())

leftMax = [0] * 2
midMax = [0] * 2
rightMax = [0] * 2
leftMin = [0] * 2
midMin = [0] * 2
rightMin = [0] * 2
dpmax, dpmin = 0, 0

for x in range(n):
    left, mid, right = map(int, input().split())
    leftMax[x%2] = max(leftMax[(x-1)%2], midMax[(x-1)%2]) + left
    midMax[x%2] = max(leftMax[(x-1)%2], midMax[(x-1)%2], rightMax[(x-1)%2]) + mid
    rightMax[x%2] = max(rightMax[(x-1)%2], midMax[(x-1)%2]) + right
    dpmax = max(leftMax[x%2], midMax[x%2], rightMax[x%2])

    leftMin[x%2] = min(leftMin[(x-1)%2], midMin[(x-1)%2]) + left
    midMin[x%2] = min(leftMin[(x-1)%2], midMin[(x-1)%2], rightMin[(x-1)%2]) + mid
    rightMin[x%2] = min(rightMin[(x-1)%2], midMin[(x-1)%2]) + right
    dpmin = min(leftMin[x%2], midMin[x%2], rightMin[x%2])
print(dpmax, dpmin)
