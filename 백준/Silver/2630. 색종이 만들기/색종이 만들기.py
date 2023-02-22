import sys

input = sys.stdin.readline

def checkSqaure(vec, h):
    total = 0
    x, y = vec
    for i in range(h):
        for j in range(h):
            total += m[y+i][x+j]

    if total == h*h:  # 모두 1인 경우
        return 1
    elif total == 0: # 모두 0인 경우
        return 0
    else: # 1,0이 섞인 경우
        return -1


def cutPaper(vec, d):
    if d == 0: return

    s = checkSqaure(vec, d)
    if s == 1:  # 모두 1일 때
        global cntBlue
        cntBlue += 1

    elif s == 0:  # 모두 0일 때
        global cntWhite
        cntWhite += 1

    else:  # 1, 0이 섞였을 때
        x, y = vec
        gap = d // 2
        a = (x, y)
        b = (x + gap, y)
        c = (x, y + gap)
        d = (x + gap, y + gap)

        cutPaper(a, gap)
        cutPaper(b, gap)
        cutPaper(c, gap)
        cutPaper(d, gap)


n = int(input())
m = [list(map(int, input().rstrip().split())) for _ in range(n)]
cntBlue,cntWhite = 0, 0
cutPaper((0,0), n)
print(cntWhite)
print(cntBlue)