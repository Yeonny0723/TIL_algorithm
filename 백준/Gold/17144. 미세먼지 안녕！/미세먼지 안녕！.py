"""
- 미세먼지가 있다면? 위/아래/좌/우 네 방향으로 미세먼지양//5 만큼 확산 발생
- 공기 청정기가 작동하면, 바람 순환 범위 내에서 미세먼지가 모두 한 칸씩 이동
- 공기 청정기로 들어간 미세먼지는 모두 정화됨
- 공기청정기는 항상 1번 열에 설치 & 크기는 두 행
"""

import copy
import sys
input = sys.stdin.readline

r, c, t = map(int, input().split())
dust = [] # 먼지 좌표
ventils = [] # 청정기 좌표 (열-세로, 행-가로)
ds = [(1,0), (-1, 0), (0, 1), (0, -1)]
m = [] # 전체 좌표
for i in range(r): # 행
    row = list(map(int, input().split()))
    m.append(row)
    for j in range(c): # 열
        if m[i][j] == -1:
            ventils.append((i, j))
        elif m[i][j] != 0:
            dust.append((i, j))


# 먼지 확산
def spread():
    diff = [[0] * c for _ in range(r)]
    for x in range(c):
        for y in range(r):
            share = m[y][x] // 5
            if m[y][x] > 0:
                cnt = 0
                for dx, dy in ds: # 상/하/좌/우
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < c and 0 <= ny < r and m[ny][nx] != -1:  # 유효한 범위에 있고 청정기가 없을 때
                        diff[ny][nx] += share
                        cnt += 1
                m[y][x] = m[y][x] - (share * cnt)
    for i in range(r):
        for j in range(c):
            m[i][j] += diff[i][j]


def move():
    temp = copy.deepcopy(m) # 원본
    # 위
    y1, x1 = ventils[0]
    m[y1][1] = 0
    for i in range(2, c):
        m[y1][i] = temp[y1][i - 1] 
    for i in range(y1 - 1, -1, -1):
        m[i][c - 1] = temp[i + 1][c - 1]
    for i in range(c - 2, -1, -1):
        m[0][i] = temp[0][i + 1]
    for i in range(1, y1):
        m[i][0] = temp[i - 1][0]

    # 아래
    y2, x2 = ventils[1]
    m[y2][1] = 0
    for i in range(2, c):
        m[y2][i] = temp[y2][i - 1]
    for i in range(y2 + 1, r):
        m[i][c - 1] = temp[i - 1][c - 1]
    for i in range(c - 2, -1, -1):
        m[r - 1][i] = temp[r - 1][i + 1]
    for i in range(r - 2, y2, -1):
        m[i][0] = temp[i + 1][0]

def count():
    ans = 0
    for x in range(c):
        for y in range(r):
            if m[y][x] > 0:
                ans += m[y][x]
    return ans

for _ in range(t):
    spread()
    move()

print(count())