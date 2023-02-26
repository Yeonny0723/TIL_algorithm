"""
맨 왼쪽 위 칸에서 -> 맨 아래 오른쪽 칸으로 이동.
항상 숫자가 더 작은 지점으로만 이동하려함.
그 경로의 개수를 구하는 문제.

어떤 방향으로 가던 상관 없음.

A점에 도착하면 목표점으로 무조건 가는 방법이 있다면,
A점의 상하좌우 지점에 도착하면, A로 이동시 무조건 방법이 있음.
각 지점별 도착 가능 여부를 저장하는 DP를 사용할 수 있겠다.
"""

import sys
input = sys.stdin.readline

def dfs(x, y):
    if x == M-1 and y == N-1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 0 # 방문 체크
    for d in ds:
        dx, dy = d
        nx = x + dx
        ny = y + dy
        if 0 <= nx < M and 0 <= ny < N and map[nx][ny] < map[x][y]:
            dp[x][y] += dfs(nx, ny)
    return dp[x][y]

M, N = map(int, input().split())
dp = [[-1] * N for _ in range(M)] # -1: 미방문 0: 방문
map = [list(map(int, input().split())) for _ in range(M)]
ds = [(1,0), (-1,0), (0,1), (0,-1)]
print(dfs(0, 0))
