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
    
n = int(input()) # N 행성 수 
m = [list(map(int,input().split())) for _ in range(n)]
parent = [i for i in range(n+1)]
edges = []
for i in range(n):
    for j in range(n):
        edges.append((m[i][j], i, j))
    
edges.sort() 

res = 0
for edge in edges:
    cost, a, b, = edge
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        res += cost
print(res)