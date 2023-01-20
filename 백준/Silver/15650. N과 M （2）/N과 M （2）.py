import sys

input = sys.stdin.readline

def canBeSelected(i): 
    # 다음 숫자로 선택될 수 있는지 점검하는 함수 
    isValid = True # 뽑았던 숫자 << 뽑으려는 숫자
    for num in ans:
        if num >= i:
            isValid = False
    return isValid


def dfs():
    if len(ans) == M:
        print(" ".join(map(str, ans)))
        return
    for i in range(1, N+1):
        isValid = canBeSelected(i)
        if not isValid: continue;
        ans.append(i)
        dfs()
        ans.pop()
        
N, M = map(int, input().split())
ans = []
dfs()