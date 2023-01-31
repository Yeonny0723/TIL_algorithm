import sys

input = sys.stdin.readline

def getMinCoinCount():
    N, K = map(int, input().rstrip().split(" "))
    coins = [int(input()) for _ in range(N)]
    count, quotient, remains = 0, 0, K
    for i in range(len(coins)-1, -1, -1):
        quotient = remains // coins[i]
        remains = remains % coins[i]
        count += quotient
    print(count)

getMinCoinCount()