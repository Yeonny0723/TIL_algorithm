import sys
input = sys.stdin.readline

N, K = map(int, input().split())
nums = [i+1 for i in range(N)]

q = []
while True: 
    idx = K-1
    while idx >= len(nums):
        idx -= len(nums)
    q.append(str(nums[idx]))
    nums = nums[idx+1:] + nums[:idx]
    if not nums:
        break
print("<"+", ".join(q)+">")