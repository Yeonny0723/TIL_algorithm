import sys
from collections import deque
input = sys.stdin.readline


def bfs(k):
    need_visit = deque([k])
    visited = [False for _ in range(n + 1)]  # 방문체크. 시도(3). 0, 1 int형이 아닌 True/False
    visited[k] = True
    cnt = 1

    while need_visit:
        x = need_visit.popleft()

        for nx in graph[x]:
            if not visited[nx]:
                visited[nx] = True # 방문 체크
                cnt += 1
                need_visit.append(nx) # 시도(2). += 재선언 대신, 기존 배열 extend

    return cnt


n, m = map(int, input().rstrip().split())
graph = [[] for _ in range(n + 1)]  # 그래프
for _ in range(m):  # 그래프 생성
    x, y = map(int, input().rstrip().split())
    graph[y].append(x)


maxV, ans = 1, []  # 최대값, 정답배열
for k in range(1, n+1):  # 최대 연결 값 찾기
    cnt = bfs(k)
    if cnt > maxV:
        maxV = cnt
        ans.clear() # 메모리 초과 시도(1). ans = [k]로 새로운 배열 메모리 생성 대신 기존 배열 수정.
        ans.append(k)
    elif cnt == maxV:
        ans.append(k)

print(*ans)
