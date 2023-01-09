import sys

input = sys.stdin.readline

N, M = map(int, input().split())
m = [list(map(int,input().split())) for _ in range(N)]
K = int(input())

for _ in range(K):
    i,j,x,y = map(int, input().split())
    
    res = 0
    for lst in m[i-1:x]:
        res += sum(lst[j-1:y])
    print(res)