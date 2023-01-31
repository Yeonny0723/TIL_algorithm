# A 300초,B 60초 ,C 10초. 3개의 버튼. 
# 총 합이 T가 되도록하는 최소 버튼 푸쉬 회수. 안되는 경우에는 -1 출력
import sys

input = sys.stdin.readline

def getBtnClicks():
    T = int(input())
    quotient, remains, ans = 0, T, []
    
    for s in [300, 60, 10]:
        quotient = remains // s
        remains = remains % s
        ans.append(quotient)

    if remains:
        print(-1)
    else:
        print(*ans)

getBtnClicks()