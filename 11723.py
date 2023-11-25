import sys
input = sys.stdin.readline
listA = set()
def add(x):
    if not x in listA:
        listA.add(x)

def remove(x):
    if x in listA:
        listA.remove(x)

def check(x):
    if x in listA:
        print(1)
    else:
        print(0)

def toggle(x):
    if x in listA:
        listA.remove(x)
    else:
        listA.add(x)

def all():
    listA.clear()
    for i in range(1,21):
        listA.add(i)

def empty():
    listA.clear()

n = int(input())

for i in range(n):
    tmp = list(input().split())
    if tmp[0] == "all" or tmp[0] == "empty":
        if tmp[0] == "all":
            all()
        if tmp[0] == "empty":
            empty()
    else:
        b = int(tmp[1])
        if tmp[0] == "add":
            add(b)
        if tmp[0] == "remove":
            remove(b)
        if tmp[0] == "check":
            check(b)
        if tmp[0] == "toggle":
            toggle(b)
        