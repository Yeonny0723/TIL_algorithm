
from collections import deque

n, m = map(int, input().split())
visited = [[[0]*2 for _ in range(m) ] for _ in range(n)]
# (x,y,z) z는 벽 부숨 여부
# visited[x][y][0]이라면 벽 안부순 누적값, visited[x][y][1]이라면 벽 부순 누적값
M = []
for _ in range(n):
    row = list(str(input().rstrip()))
    M.append(list(map(int, row)))

ds = [(1,0), (-1,0), (0,-1), (0, 1)]

def bfs(x,y,z):
    q = deque()
    q.append((x,y,z))
    visited[x][y][z] = 1

    while q:
        x, y, w = q.popleft()

        if x == n - 1 and y == m - 1: # 목표 지점 도달
            return visited[x][y][w]

        for d in ds:
            nx, ny = x + d[0], y + d[1]

            if 0 <= nx < n and 0 <= ny < m: # 유효 범위 내 있다면
                # 이동 가능 & 방문 X
                if M[nx][ny] == 0 and visited[nx][ny][w] == 0:
                    visited[nx][ny][w] = visited[x][y][w] + 1
                    q.append((nx, ny, w))

                # 이동 불가 & 벽 부술 수 있음
                elif M[nx][ny] == 1 and w == 0:
                    visited[nx][ny][w + 1] = visited[x][y][w] + 1
                    q.append((nx, ny, w + 1)) # 벽 부숨

    return -1 # 불가능

print(bfs(0,0,0))
