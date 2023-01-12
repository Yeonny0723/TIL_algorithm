from collections import deque
import sys

input = sys.stdin.readline

def solution(): 
    N = int(input())
    nums = deque([i for i in range(N, 0, -1)])

    while len(nums) > 1: 
        nums.pop()
        nums.appendleft(nums.pop())
    
    print(*nums)

solution()