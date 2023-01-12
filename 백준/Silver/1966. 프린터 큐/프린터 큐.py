from collections import deque # fifo, lilo 모두 구현 가능. list 보다 빠르게 설계
import sys

input = sys.stdin.readline

def solution():
    for _ in range(int(input())):
        N, M = map(int, input().split())
        rank_lst = list(map(int, input().split())) # 중요도 리스트
        rank_tup = deque([(rank, idx) for idx, rank in enumerate(rank_lst)]) # (중요도, 인덱스) 큐

        count = 0 # 출력 번호
        while True:
            maxTuple = max(rank_tup, key= lambda x:x[0]) # 최대 rank(중요도) 포함 튜플 
            if rank_tup[0][0] == maxTuple[0]: # 첫 원소의 우선순위가 최대라면
                if rank_tup[0][1] == M: # 최대값 인덱스가 맨 첫 원소 인덱스와 같다면 
                    count += 1
                    break
                else: 
                    rank_tup.popleft()
                    count += 1
            else:
                rank_tup.append(rank_tup.popleft())
        print(count)
        
solution()