import sys
import heapq
input = sys.stdin.readline

v, e = map(int, input().rstrip().split())  # V 정점 E 간선
start = int(input())  # 시작점
INF = int(1e9)
costs = [INF] * (v+1)
graph = [[] for _ in range(v+1)]  # 그래프 생성
for _ in range(e):
    u, v, cost = map(int, input().rstrip().split())
    graph[u].append((v, cost))  # heapq는 cost 기준 자동 오름차순 정렬

q = []
costs[start] = 0  # 시작노드에서 시작노드로 가는 비용
heapq.heappush(q, (costs[start], start))  # 비용, 노드
while q:
    cost, node = heapq.heappop(q)
    for nxt in graph[node]:
        nxtNode, nxtCost = nxt
        newCost = cost + nxtCost
        if newCost > costs[nxtNode]: # 크다면 넘기고
            continue
        costs[nxtNode] = newCost  # 작다면 갱신
        heapq.heappush(q, (newCost, nxtNode))

for cost in costs[1:]:
    if cost == INF:
        print("INF")
    else:
        print(cost)
