import sys

input = sys.stdin.readline

N = int(input())

nums = []
for _ in range(N):
    new_num = int(input())
    if nums: 
        while nums[-1] <= new_num:
            nums.pop() # 마지막 원소보다 크거나 작은 경우 모두 제외 
            if not nums: break
        nums.append(new_num) 
    else:
        nums.append(new_num)

print(len(nums))