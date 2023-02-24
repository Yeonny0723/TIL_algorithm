import sys

input = sys.stdin.readline

def getStats(arr):
    """
    팀의 총 능력치를 구하는 함수
    :param arr: 팀 멤버
    :return: 팀 총 능력치
    """
    stats = 0
    n = len(arr)
    for i in range(n-1):
        for j in range(i, n):
            x = arr[i]
            y = arr[j]
            stats += m[x][y]
            stats += m[y][x]

    return stats


def dfs():
    if len(startT) == n // 2:
        linkT = [i for i in range(n) if i not in startT]
        global minGap
        _gap = abs(getStats(startT)-getStats(linkT))
        minGap = min(_gap, minGap)
        return

    for i in range(n):
        if i in startT:
            continue

        if not startT or i > startT[-1]: # 팀원 뽑기를 한방향으로 제한
            startT.append(i)
            dfs()
            startT.pop() # 백트레킹

n = int(input())
m = [list(map(int, input().rstrip().split())) for _ in range(n)]
minGap, startT = int(1e8), [] # 스타트팀 선수
dfs()
print(minGap)