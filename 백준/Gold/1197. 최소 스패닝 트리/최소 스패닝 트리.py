def find_parent(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find_parent(parent[x])
        return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a
        
v, e = map(int, input().split())
parent = [i for i in range(v+1)] # 부모값을 자기자신으로 초기화
edges = []
res = 0

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b)) 
    
edges.sort()

for edge in edges: # 간선 완전 탐색 (사이클 존재 여부 확인)
    cost, a, b = edge
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        res += cost

print(res)