import sys

input = sys.stdin.readline
count =0
n, k = map(int, input().split())
listCoin = []

for i in range(n):
    coin = int(input())
    listCoin.append(coin)

listCoin.sort(reverse=True)

for coins in listCoin:
    count += k // coins
    k %= coins

print(count)