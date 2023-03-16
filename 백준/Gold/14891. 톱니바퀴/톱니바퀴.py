from collections import deque
import sys

input = sys.stdin.readline

gears = [deque(list(map(int,list(input().rstrip())))) for _ in range(4)]
k = int(input()) # 톱니 회전 개수

for _ in range(k):
    n, d = map(int, input().split()) # 톱니 바퀴, 회전 방향
    n -= 1 # 톱니 바퀴 인덱스
    r, l = gears[n][2], gears[n][6] # 왼쪽 톱니, 오른쪽 톱니
    gears[n].rotate(d) 
    lst = [] # 맞닿을 수있는 좌우 톱니 극 저장

    nd = d
    for i in range(n-1, -1, -1): # 왼쪽에 있는 바퀴들
        if gears[i][2] != l:		# 서로 다른 극인 경우
            l = gears[i][6]
            gears[i].rotate(nd*-1)
            nd *= -1
        else:
            break

    nd = d
    for i in range(n+1, 4): # 오른쪽에 있는 바퀴들
        if gears[i][6] != r: # 서로 다른 극인 경우
            r = gears[i][2]
            gears[i].rotate(nd*-1)
            nd *= -1
        else:
            break

ans = 0
for i in range(4):
    if gears[i][0] == 1:
        ans += (2**i)

print(ans)