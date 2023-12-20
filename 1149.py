"""
답을 구하기 위해 필요한 정보를 역으로 추적해나가는 과정
먼저, 구하고자 하는 답은 1번 집부터 N번 집까지 색칠하는 비용의 최솟값. f(x) = "1번 집부터 x번 집까지 색칠하는 비용의 최솟값" 으로 정의.
이제 f(x)를 f(x-1), f(x-2) 등등의 이전 함숫값으로부터 구하려면 어떻게 해야 할지 생각해야 함
f에 대해 조금 더 생각... N개의 집에 색을 어떻게 칠하든, 마지막 집의 색을 R, G, B 세 종류 중 하나로 칠했음. 
각각의 경우마다 비용을 따로 모아볼 수 있을텐데, 
전체의 최솟값 (= f)은 마지막 집 색을 R로 고정하고 비용을 최소로 한 경우이거나, 아니면 G/B로 고정하고 마찬가지로 구한 세 경우 중 하나여야 함.
마지막 집의 색을 R/G/B로 고정했을 때 1~x까지의 집을 색칠하는 비용의 최솟값을 각각 r(x), g(x), b(x)라 한다면 다음이 성립함.
f(x) = min(r(x), g(x), b(x))
이웃한 집의 색이 달라야 하니, 마지막 집의 색이 R이었다면 그 직전 집의 색은 G 혹은 B. 
이걸 바탕으로 식을 세우면,
r(x) = min(g(x-1), b(x-1)) + (마지막 집을 R로 칠하는데 든 비용)
마찬가지로 g(x), b(x)도 똑같은 방식으로 세우면 됨
"""
import sys
input = sys.stdin.readline

n = int(input().strip())
listA = [[] for _ in range(n)]
r = [0] * n
g = [0] * n
b = [0] * n
for i in range(n):
    x, y, z = map(int, input().split())
    listA[i] = [x,y,z]
f = [0] * n
r[0] = listA[0][0]
g[0] = listA[0][1]
b[0] = listA[0][2]
for x in range(1,n):
    r[x] = min(g[x-1],b[x-1]) + listA[x][0]
    g[x] = min(r[x-1],b[x-1]) + listA[x][1]
    b[x] = min(g[x-1],r[x-1]) + listA[x][2]
    f[x] = min(r[x],g[x],b[x])

print(f[-1])