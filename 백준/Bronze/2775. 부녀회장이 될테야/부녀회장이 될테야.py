#k층 n호 거주자수 == k-1층의 1~n호까지 거주자수
# f(k,n) = f(k-1, 1) + f(k-1,2)... + f(k-1,n)

import sys

input = sys.stdin.readline

def countPpl():    
    k = int(input().rstrip()) # 층 
    n = int(input().rstrip()) # 호
    cache = [[None for _ in range(n+1)] for _ in range(k+1)]
    # cache = [[None for _ in range(n+1)]] * (k+1) # <- 참조값까지 복사되는 문제 
    cache[0] = [i for i in range(n+1)] # 0층 초기화
    
    for i in range(1, k+1): # 층
        for j in range(1, n+1): # 호
            if not cache[i][j]: # 없으면
                cache[i][j] = sum(cache[i-1][1:j+1])
            else: 
                continue
            
    print(cache[k][n])
    

for _ in range(int(input())):
    countPpl();