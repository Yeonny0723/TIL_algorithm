from collections import deque

def bfs():
    need_visit = deque([s])
    visited[s] = 1

    while need_visit:
        x = need_visit.popleft()

        if x == g:
            return counts[x]

        for dx in [u, -d]:
            nx = x + dx
            if nx > f or nx < 1 or visited[nx]:
                continue
            visited[nx] = 1
            counts[nx] = counts[x] + 1 # 그 다음 층을 가는 경우
            need_visit.append(nx)

    if counts[g] == 0:
        return 'use the stairs'

f, s, g, u, d = map(int, input().split())
visited = [0 for _ in range(f + 1)] # 방문 체크
counts = [0 for _ in range(f + 1)] # s층에서 각 층을 갈 수 있는 최소 이동값 (dp)
print(bfs())
