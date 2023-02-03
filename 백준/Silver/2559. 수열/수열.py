import sys

input = sys.stdin.readline

N, K = map(int, input().rstrip().split(" "))
nums = list(map(int, input().split(" ")))

total = sum(nums[:K]) 
maxTotal = total
for i in range(K, N):
    total += nums[i]
    total -= nums[i-K]
    maxTotal = max(maxTotal, total)

print(maxTotal)