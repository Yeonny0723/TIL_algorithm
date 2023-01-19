from itertools import combinations
import sys

input = sys.stdin.readline

while True: 
    nums = list(map(int, input().rstrip().split()))
    if not len(nums):
        break
    k = nums[0]
    s = nums[1:]   
    
    subsets = sorted(list(combinations(s, 6)))
    for subset in subsets:
        print(*subset)
    print()