import sys

input = sys.stdin.readline

def solution():
    nums = [0]* 10000
    for _ in range(int(input())):
        idx = int(input()) - 1
        nums[idx] += 1
        
    for idx, num in enumerate(nums):
        for _ in range(num):
            print(idx+1)

solution()