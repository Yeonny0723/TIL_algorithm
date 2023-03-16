"""
필요한 물건: n개
각 물건의 무게 w, 가치 v

최대 k 무게 만큼 넣을 수 있을 때,
넣을 수 있는 물건 '가치'의 최댓 값을 구하는 문제
"""

n, k = map(int, input().split()) # 필요한 물건 개수, 최대 가방 무게
items = [(0,0)]
for _ in range(n):
    items.append(tuple(map(int, input().split())))

d = [[0]*(k+1) for _ in range(n+1)]
# d[i][j]- i개의 물건의 허용 무게가 j일 때 배낭의 최대 가치

for i in range(1, n+1): # 물건 순회
    w = items[i][0] # 새 물건 무게
    v = items[i][1] # 새 물건 가치

    for j in range(1, k+1): # 무게 순회 (허용 무게)
        if j < w: # 새 물건 무게가 허용 무게보다 큰 경우
            # 현재 물건을 넣지 않고 그대로
            d[i][j] = d[i-1][j]
        else: # 새 물건의 무게가 더 작다면
            # 현재 넣을 무게만큼 배낭에서 빼고 현재 물건을 넣음
            d[i][j] = max(d[i-1][j], d[i-1][j-w]+v)

print(d[n][k])
