n, m = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)] # 최대값 갱신
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                graph[i][j] = 0
            else:
                graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

result = [0] * (n + 1)
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i != j:
            result[i] += graph[i][j]

print(result.index(min(result[1:])))