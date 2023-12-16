import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    listA = list(map(int, input().split()))
    visited = [False] * n
    ans = []
    ans2 = []

    def back(start):
        if len(ans) == m:
            ans2.append(ans[:])
            return
        for i in range(len(listA)):
            if not visited[i]:
                visited[i] =True
                ans.append(listA[i])
                back(i)
                visited[i] = False
                ans.pop()
        return 
    back(-1)
    ans2 = sorted(list(set(map(tuple,ans2))))
    for i in ans2:
        print(*i, sep=' ')



if __name__ == '__main__':
    main()