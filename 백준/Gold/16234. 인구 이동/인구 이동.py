"""
땅과 각 나라의 인구 수가 주어짐.
인구 이동이 진행됨.
인접한 나라의 인구 수 차이가 L이상 R이하 -> 국경을 열고 -> 인구 이동

출력값:
인구 이동이 며칠 동안 발생하는지 출력
"""
from collections import deque
import sys

input = sys.stdin.readline

def move(a,b): # (a,b)를 시작점으로 이어진 좌표 구하기
    q = deque()
    q.append((a,b))
    vecs = []
    vecs.append((a,b))
    total = m[a][b]
    len = 1
    while q:
        x, y = q.popleft()
        for dx, dy in ds:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if l <= abs(m[x][y] - m[nx][ny]) <= r:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    vecs.append((nx, ny))
                    total += m[nx][ny]
                    len += 1

    return vecs, total // len


n, l, r = map(int, input().rstrip().split())
m = [list(map(int, input().rstrip().split())) for _ in range(n)]
ds = [(1,0), (-1,0), (0,1), (0,-1)]
cnt = 0
while True:
    visited = [[0]*(n) for _ in range(n)]
    flag = False
    for i in range(n): # 모든 좌표 순회
        for j in range(n):
            if visited[i][j]: continue
            visited[i][j] = 1
            vecs, nums = move(i, j)
            if len(vecs) > 1:
                flag = True
            for x, y in vecs:
                m[x][y] = nums

    if not flag: break
    cnt += 1

print(cnt)