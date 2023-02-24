import sys
input = sys.stdin.readline


def dfs(cost):
    if len(visited) == n:
        start, end = visited[0], visited[-1]
        if m[end][start]:
            global minV
            minV = min(minV, cost + m[end][start])
        return

    _cost = cost
    for i in range(n):
        if i in visited:
            continue

        if visited:
            end = visited[-1]
            if m[end][i]:
                _cost += m[end][i]
            else:
                continue

        visited.append(i)
        dfs(_cost)
        visited.pop()
        _cost = cost

n = int(input())
m = [list(map(int, input().rstrip().split())) for _ in range(n)]
minV = int(1e9)
visited = []
dfs(0)
print(minV)