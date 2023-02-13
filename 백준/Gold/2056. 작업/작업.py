"""
소요되는 시간의 최소값은, 
선행관계에 있는 작업들 중 가장 늦게 끝나는 작업 + 현재 작업 = 현재 작업이 끝나는 시간
"""
import sys
from collections import deque

input = sys.stdin.readline

def topological_sort():
    
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = costs[i]
            
    while q:
        node = q.popleft()
        for nxtNode in graph[node]:
            indegree[nxtNode] -= 1
            dp[nxtNode] = max(dp[node] + costs[nxtNode], dp[nxtNode])
            if indegree[nxtNode] == 0:
                q.append(nxtNode)
    
    return max(dp)
    
if __name__ == "__main__":
    n = int(input())
    indegree = [0] * (n+1)
    costs = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    dp = [0] * (n+1) 
    for node in range(1,n+1):
        lst = list(map(int, input().rstrip().split()))
        iTime, iIndegree = lst[0], lst[1] # 소요시간, 선행작업수
        costs[node] = iTime
        indegree[node] = lst[1] # 이전 개수  
        if indegree == 0:
            continue
        for pre in lst[2:]:
            graph[pre].append(node)
    
    print(topological_sort())