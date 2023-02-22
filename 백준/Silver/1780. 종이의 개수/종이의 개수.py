import sys
input = sys.stdin.readline

def getTotal(vec, h):
    x, y = vec
    isZero, isOne, isMinus, isMixed = False, False, False, False

    for i in range(h):
        for j in range(h):
            t = m[y+i][x+j]
            if t == 0:
                isZero = True
            elif t == 1:
                isOne = True
            elif t == -1:
                isMinus = True

    if sum([isZero, isOne, isMinus]) > 1: # True가 한개 이상 -> 섞임
        return 2 # 섞임

    else:
        if isZero: return 0
        if isOne: return 1
        if isMinus: return -1

def cutPaper(vec, h):
    x, y = vec

    if h == 0:
        return

    state = getTotal(vec, h)

    if state == 0:
        global cnt0
        cnt0 += 1

    elif state == 1:
        global cnt1
        cnt1 += 1

    elif state == -1:
        global cntN1
        cntN1 += 1

    else:
        for d in ds:
            _h = h // 3
            cutPaper((x+_h*d[0], y+_h*d[1]), _h)

n = int(input())
m = [list(map(int,input().rstrip().split())) for _ in range(n)]
cnt0, cnt1, cntN1 = 0, 0, 0
ds = [(0,0),(1,0),(2,0),(0,1),(1,1),(2,1),(0,2),(1,2),(2,2)]

cutPaper((0,0), n)
print(cntN1)
print(cnt0)
print(cnt1)
