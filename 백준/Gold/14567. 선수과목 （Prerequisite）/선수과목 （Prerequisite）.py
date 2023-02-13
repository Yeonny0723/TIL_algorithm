"""
선수과목  조건을 지키며 모든 과목을 이수하기 위해 걸리는 최소 학기
(사이클이 없는 유-방향 그래프 문제)
"""
import sys
from collections import deque

input = sys.stdin.readline

def topology_sort():
    order = [0] * (n+1)
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0: # 진입차수가 0인 노드 추가
            q.append((i, 1)) # i 과목, 1 학기
    
    while q:
        node, sem = q.popleft()
        order[node] = (node, sem)
        for nxtNode in graph[node]:
            indegree[nxtNode] -= 1
            if indegree[nxtNode] == 0:
                q.append((nxtNode, sem+1))

    return " ".join([str(tpl[1]) for tpl in order[1:]])


n, m = map(int, input().rstrip().split()) # n: 과목 수, m: 선수조건수
indegree = [0] * (n+1) # 진입차수
graph = [[] for _ in range(n+1)] # 그래프
for _ in range(m):
    nodeFrom, nodeTo = map(int, input().rstrip().split())
    graph[nodeFrom].append(nodeTo)
    indegree[nodeTo] += 1
    
print(topology_sort()) # 결과 출력