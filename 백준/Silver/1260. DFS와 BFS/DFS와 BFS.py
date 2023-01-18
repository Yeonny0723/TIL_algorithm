import sys
from collections import defaultdict, deque

input = sys.stdin.readline

def BFS(graph, V):
    '''
    너비 우선 탐색 
    Queue 활용 
    '''
    visited = defaultdict(lambda:0)  # 1: 방문, 0: 미방문
    needVisit = deque([V])
    
    while needVisit:
        node = needVisit.popleft()
        if visited[node] == 0:
            visited[node] = 1
            needVisit.extend(graph[node])   
            
    return visited.keys()


def DFS(graph, V):
    '''
    깊이 우선 탐색 
    재귀 활용
    '''
    visited = defaultdict(lambda:0)  # 1: 방문, 0: 미방문
    needVisit = [V]
    
    while needVisit:
        node = needVisit.pop()
        if visited[node] == 0:
            visited[node] = 1
            needVisit.extend(list(reversed(graph[node]))) # 작은 수부터 방문함. 따라서 오름차순으로 정렬된 숫자를 뒤집어 extend
            
    return visited.keys()


def init():
    N, M, V = map(int, input().split()) 
    # 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V
    graph = defaultdict(list)

    for _ in range(M):
        k, v = map(int, input().split())
        graph[k].append(v)
        graph[v].append(k)

    for k, v in graph.items():
        graph[k].sort() # 연결된 간선을 정렬. 방문 시 작은 것부터 먼저 방문하게 하기 위함

    print(" ".join(map(str,DFS(graph, V))))
    print(" ".join(map(str,BFS(graph, V))))
    

init()