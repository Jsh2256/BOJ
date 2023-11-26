import sys
input = sys.stdin.readline

t = int(input())
dicA = {}


for _ in range(t):
    n = int(input())
    count=1
    dicA.clear()
    for i in range(n):
        name, kind = map(str, input().split())
        if not kind in dicA.keys():
            dicA[kind]=[name]
        else:
            dicA[kind].append(name)
    for j in dicA:
        count *= (len(dicA[j])+1)
        
    
    print(count-1)
