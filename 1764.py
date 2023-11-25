n, m = map(int, input().split())

listNotListen = []
listNotLook = []
for i in range(n+m):
    if i < n:
        tmp = input()
        listNotListen.append(tmp)
    else:
        tmp = input()
        listNotLook.append(tmp)

a = set(listNotLook)
b = set(listNotListen)
x = list(a.intersection(b))

x.sort()
print(len(x))
print(*x, sep="\n")