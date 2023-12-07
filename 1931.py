import sys
input = sys.stdin.readline

n = int(input())
listc = []
listA = []
for _ in range(n):
    s, e = map(int, input().split())
    listc.append([s, e])
for i in listc:
    #if i not in listA:  
        listA.append(i)
listA.sort()

#print(listA)
for i in range(len(listA)-1):
    if listA[i][1] > listA[i+1][1]:
        listA[i], listA[i+1] = listA[i+1], listA[i]
#print(listA)
#for i in range(len(listA)-1):
#    if listA[i]==listA[i+1]:
#        listA.pop(i+1)
#print(listA)
listB = [-1]
cnt=0
for i in listA:
    if i[0] >= listB[-1]:
        if i[1] == i[0]:
            #if not i[0] in listB:
                listB.append(i[0])
                cnt+=1
        else:
            for j in range(i[0], i[1]+1):
                #if not j in listB:
                    listB.append(j)
            cnt+=1
        

print(cnt)