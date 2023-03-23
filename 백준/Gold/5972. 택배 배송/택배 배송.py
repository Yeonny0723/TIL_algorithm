"""
다익스트라 알고리즘
- 매 순간 (방문하지 않은 노드 중) 비용이 가장 작은 노드 선택
- 선택한 노드를 거쳐 가는 비용과, 거치지 않고 가는 비용과 비교 후 최소 비용 갱시
"""

import heapq
import sys

def move(start):
    q = []
    heapq.heappush(q, (0, start))
    costs[start] = 0
    while q:
        cost, node = heapq.heappop(q)
        if costs[node] < cost:
            continue
        for nxt in graph[node]:
            nxtNode, nxtCost = nxt
            newCost = cost + nxtCost
            if newCost < costs[nxtNode]:
                costs[nxtNode] = newCost
                heapq.heappush(q, (newCost, nxtNode))

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
INF = int(1e9)
costs = [INF]*(N+1) # 1에서 각 노드로의 이동 비용
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c)) # a -> b 이동 비용 c.
    graph[b].append((a, c))

move(1)
print(costs[N])