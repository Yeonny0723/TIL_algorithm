"""
가장 많은 빌딩이 보이는 고층 빌딩을 찾으려 함.

다른 건물이 보이는 조건?
- 왼쪽: 기준 건물과 그 다음 탐색하는 건물의 기울기보다 더 작을 때
- 오른쪽: 기준 건물과 그 다음 탐색하는 건물의 기울기보다 더 클 때
"""

import sys
input = sys.stdin.readline

def getSlope(x1,y1,x2,y2):
    return (y2-y1)/(x2-x1)


def solution():
    N = int(input())
    building = list(map(int, input().split()))
    INF = sys.maxsize
    ans = 0
    for idx, target in enumerate(building): # 모든 빌딩 순회
        cnt = 0  # 보이는 빌딩 카운트
        # 왼쪽 빌딩
        left = INF # 기울기 최소
        for i in range(idx - 1, -1, -1):  # 왼쪽
            c = getSlope(idx + 1, target, i + 1, building[i])
            if c < left:  # 기울기가 더 작다면
                left = c
                cnt += 1
    
        # 오른쪽 빌딩
        right = -INF  # 기울기 최대
        for i in range(idx + 1, N):  # 오른쪽
            c = getSlope(idx + 1, target, i + 1, building[i])
            if c > right:  # 기울기가 더 크다면
                right = c
                cnt += 1
    
        ans = max(ans, cnt)
    
    return ans
    
print(solution())