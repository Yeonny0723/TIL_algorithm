"""
모든 노드를 순회하며, 누적 비용 구한 후, 그 중 최소값을 출력
선행관계에 있는 작업들 중 가장 늦게 끝나는 작업 + 현재 작업 = 현재 작업이 끝나는 시간
"""

n = int(input())
costs = [0 for _ in range(n+1)] # 비용
graph = [[] for _ in range(n+1)] # 그래프 
for node in range(1, n+1): # 이전 노드를 배열로 갖는 그래프 생성 
    cost, m, *lst = map(int, input().split()) # 비용, 이전노드개수
    costs[node] = cost
    for preNode in lst:
        graph[node].append(preNode) 
        
for node in range(1, n+1): # 모든 노드 순회
    newCost = 0 
    for preNode in graph[node]: # 이전 노드 순회
        newCost = max(newCost, costs[preNode]) # 이전 노드의 
    costs[node] += newCost
print(max(costs)) 

