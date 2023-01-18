import sys

input = sys.stdin.readline

def bfs(i,j,high):
    stk = [(i,j)]
    global visited
    visited[i][j] = 1
    while stk: 
        i,j = stk.pop()
        for di, dj in [[1,0],[-1,0],[0,1],[0,-1]]:
            newi = di + i # 인접한 원소 인덱스 
            newj = dj + j
            if (0<=newi<N) and (0<=newj<N): # 유효한 인덱스 
                if (M[newi][newj] >= high): # 기준 높이보다 크거나 같은지  
                    if visited[newi][newj] == 0: # 방문한 적 없는지 
                        stk.append((newi, newj))
                        visited[newi][newj] = 1
                        
N = int(input())
M = [list(map(int, input().split())) for _ in range(N)]

highs = [] # 기준높이가 될 수 있는 숫자 추출
for row in M:
    highs += row    
highs = set(highs) # convert list -> set time complexity: O(N) https://myprogrammingtutorial.com/convert-list-to-set-python/


counts = []
for high in highs:
    visited = [[0]*N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if (visited[i][j] == 0) and (M[i][j] >= high): # 기준 높이보다 크거나 같고, 방문한 적 없다면
                bfs(i, j, high)
                count += 1
    counts.append(count)

print(max(counts))