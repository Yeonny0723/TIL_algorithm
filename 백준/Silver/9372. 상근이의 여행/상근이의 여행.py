import sys

input = sys.stdin.readline

def dfs(start, cnt): 
    visited[start] = 1
    for node in tree[start]:
        if visited[node] == 0:
            cnt = dfs(node, cnt+1)
    return cnt

for _ in range(int(input())):
    n, m = map(int, input().rstrip().split(" "))
    visited = [0] * (n+1) # 방문 체크
    tree = [[] for _ in range(n+1)] # 트리 생성
    for _ in range(m):
        k, v = map(int, input().rstrip().split(" "))
        tree[k].append(v) # 무방향
        tree[v].append(k)
    
    cnt = dfs(1, 0) # 탐색 실행
    print(cnt)