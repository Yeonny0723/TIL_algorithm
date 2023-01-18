import sys

input = sys.stdin.readline

def dfs(i,j):
    stk = [(i,j)]
    visited[j][i] = 1
    while stk:
        i, j = stk.pop()
        for di, dj in [(1,0),(-1,0),(0,1),(0,-1),(-1,1),(1,1),(-1,-1),(1,-1)]: # 가능한 변화량
            ni = di + i
            nj = dj + j
            if (0<=ni<w) and (0<=nj<h): # 유효한 인덱스라면
                if M[nj][ni] == 1: # 육지라면
                    if visited[nj][ni] == 0: # 방문한 적 없다면
                        stk.append((ni,nj))
                        visited[nj][ni] = 1
                        
while True:
    w, h = map(int, input().split())
    
    if w == h == 0:
        break
        
    M = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0]*w for _ in range(h)]
    count = 0
    for i in range(w): # x축
        for j in range(h): # y축
            if (visited[j][i] == 0) and (M[j][i] == 1): # 방문한적이 없고 유지라면
                dfs(i, j)
                count += 1
    print(count)