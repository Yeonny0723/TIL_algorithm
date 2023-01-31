import sys

input = sys.stdin.readline

def solution():
    for _ in range(int(input())):
        candidates = [tuple(map(int, input().rstrip().split(" "))) for _ in range(int(input()))]
        candidates.sort() # 1차 점수 기준 정렬
        length = len(candidates)
        
        count = 1
        nxtMin = candidates[0][1] 
        
        for idx in range(1, length):
            if candidates[idx][1] < nxtMin:
                count += 1
                nxtMin = candidates[idx][1]
        
        print(count)
    
solution()