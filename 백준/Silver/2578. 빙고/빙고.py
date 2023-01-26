import sys

input = sys.stdin.readline

def solution():
    m = [list(map(int,input().split())) for i in range(5)]
    
    d = []
    for i in range(5):
        d += list(map(int,input().split())) 
    
    bing = 0
    vectors = [] # 부른 좌표 저장 배열
    for idx, k in enumerate(d):
        for i in range(5):
            for j in range(5):
                if m[i][j] == k: # 부른 숫자의 죄표
                    count1, count2, count3, count4 = 0,0,0,0
                    for vec in vectors:
                        _x, _y = vec
                        if (_x - i == 0) and (_y - j != 0): # x가 동일
                            count1 += 1
                        if (_x - i != 0) and (_y - j == 0): # y가 동일
                            count2 += 1
                        if (_x-i) == -(_y-j): # 오른쪽 대각선 (|)
                            count3 += 1
                        if (_x-i) == (_y-j): # 왼쪽 대각선 (/)
                            count4 += 1
                    
                    for c in [count1, count2, count3, count4]:
                        if c == 4:
                            bing += 1
                            if bing == 3: # 빙고가 3개일 때 
                                return idx + 1
                    
                    vectors.append((i,j))

print(solution())