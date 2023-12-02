import sys
input = sys.stdin.readline

n = int(input())

dicA = []

for i in range(n):
    a, b = map(str, input().split())
    dicA.append([int(a),i,b])
dicA.sort()
for i in dicA:
    print(i[0], i[2])
