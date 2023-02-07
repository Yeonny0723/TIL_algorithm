import heapq
import sys

input = sys.stdin.readline

n = int(input())
votes1 = int(input()) # 1번 표 수
ranks = []
for _ in range(n-1):
    n = int(input()) # 다른 후보 표 수
    heapq.heappush(ranks, -n) # 음수로 저장
    
cnt = 0
while True:
    if not ranks:
        print(cnt)
        break
    _votes = -(heapq.heappop(ranks))
    if votes1+cnt > _votes:
        print(cnt)
        break
    else:
        _votes -= 1
        cnt += 1
        heapq.heappush(ranks, -(_votes))