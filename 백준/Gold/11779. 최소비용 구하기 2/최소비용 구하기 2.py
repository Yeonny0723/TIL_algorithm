"""
40% 메모리 초과...
"""

import sys
import heapq
input = sys.stdin.readline

def dijkstra(start, end):
    q = []
    costs[start] = 0
    heapq.heappush(q, (0, start, []))
    while q:
        cost, node, _visited = heapq.heappop(q)
        if node == end:
            visited = [*_visited, end]
            length = len(visited)
            return [costs[end], length, visited]

        for nxt in graph[node]:
            nxtNode, nxtCost = nxt
            newCost = cost + nxtCost
            newVisited = [*_visited, node]
            if newCost >= costs[nxtNode]:
                continue
            costs[nxtNode] = newCost
            heapq.heappush(q, (newCost, nxtNode, newVisited))

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
costs = [int(1e8) for _ in range(n+1)]
for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))

start, end = map(int, input().split())
minCost, cnt, nodes = dijkstra(start, end)

print(minCost)
print(cnt)
print(*nodes)