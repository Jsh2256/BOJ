import sys
import re
input = sys.stdin.readline

listA = input().strip()
listB = list(listA)
listC = []
for i in listB:
    if i == '-' or i == '+':
        listC.append(i)

for i in range(len(listC)):
    if listC[i] =="-":
        for j in range(i+1,len(listC)):
            if listC[j]=='+':
                listC[j]='-'
            else:
                break
susik = re.split(r'-|\+', listA)

for i in range(len(susik)):
    susik[i] = int(susik[i])

listD = []
susik.reverse()
listC.reverse()
for i in range(len(susik)+len(listC)):
    if i%2==0:
        listD.append(susik.pop())
    else:
        listD.append(listC.pop())
sum = 0
if len(listD)>1:
    for i in range(len(listD)):
        if i==1:
            if listD[i]=='-':
                sum+=listD[i-1]-listD[i+1]
            else:
                sum+=listD[i-1]+listD[i+1]
        elif i%2==1:
            if listD[i]=='-':
                sum-=listD[i+1]
            else:
                sum+=listD[i+1]
else:
    sum+=listD.pop()
print(sum)