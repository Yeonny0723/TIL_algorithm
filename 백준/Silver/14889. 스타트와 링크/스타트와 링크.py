import sys

input = sys.stdin.readline

def getStats(arr):
    stats = 0
    n = len(arr)
    for i in range(n-1):
        for j in range(i, n):
            x = arr[i]
            y = arr[j]
            stats += m[x][y]
            stats += m[y][x]

    return stats


def dfs(k):
    if k == n // 2:
        team2 = [i for i in range(n) if i not in team]
        global ans
        ans = min(abs(getStats(team)-getStats(team2)), ans)
        return

    for i in range(n):
        if i in team:
            continue

        if not team or i > team[-1]: # 한방향으로 제한
            k += 1
            team.append(i)
            dfs(k)
            k -= 1
            team.pop()

n = int(input())
m = [list(map(int, input().rstrip().split())) for _ in range(n)]
ans, team = int(1e8), [] # 스타트팀 선수가 담기는 곳
dfs(0)
print(ans)
