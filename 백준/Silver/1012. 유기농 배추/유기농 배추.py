import sys

input = sys.stdin.readline

def bfs(i,j):
    stk = [(i,j)]
    visited[j][i] = 1
    while stk:
        i, j = stk.pop()
        for di, dj in [[1,0],[-1,0],[0,1],[0,-1]]:
            newi = di + i # 인접한 원소 인덱스 
            newj = dj + j
            if (0<=newi<M) and (0<=newj<N): # 유효한 인덱스 
                if (grounds[newj][newi] == 1): # 배추가 있는지
                    if visited[newj][newi] == 0: # 방문한 적 없는지 
                        stk.append((newi, newj))
                        visited[newj][newi] = 1

for _ in range(int(input())):
    M, N, K =  map(int, input().rstrip().split()) # M가로 N세로 K배추있는지역수

    grounds = [[0]*M for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().rstrip().split())
        grounds[y][x] = 1

    count = 0
    for i in range(M):
        for j in range(N):
            if (grounds[j][i] == 1) and visited[j][i] == 0: # 배추가 있고 아직 방문하지 않았다면
                bfs(i,j)
                count += 1
    print(count)