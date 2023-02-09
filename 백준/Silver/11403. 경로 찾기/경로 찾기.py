from collections import defaultdict
import sys
input = sys.stdin.readline

def bfs(start):
    visited = [0 for _ in range(n)]
    need_visit = [start]
    isStart = True
    while need_visit:
        node = need_visit.pop(0)
        if visited[node]:
            continue
        
        if not isStart:
            visited[node] = 1
        else:
            isStart = False
            
        need_visit.extend(graph[node])
    
    return visited


n = int(input())
graph = defaultdict(list)
for i in range(n):
    lst = list(map(int, input().rstrip().split(" ")))
    for idx,j in enumerate(lst):
        if j: # j = 1이면
            graph[i].append(idx)
            
for i in range(n):
    print(*bfs(i))