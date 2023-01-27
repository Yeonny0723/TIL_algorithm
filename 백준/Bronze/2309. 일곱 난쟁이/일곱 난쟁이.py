import sys

input = sys.stdin.readline

def qsort(nums):
    if len(nums) <= 1:
        return nums
    pivot = nums[0]
    left = [num for num in nums[1:] if pivot > num]
    right = [num for num in nums[1:] if pivot <= num]
    return qsort(left) + [pivot] + qsort(right)

def solution():
    heights, total = [], 0
    for _ in range(9):
        height = int(input().rstrip())
        heights.append(height)
        total += height

    isFound = False
    for i in range(9):
        for j in range(0, i):
            if total == (100 + heights[i] + heights[j]):
                heights[i], heights[j] = 0,0 # 가짜 난쟁이 키는 0으로 치환
                isFound = True
                break # break inner loop
        if isFound:
            break # break outer loop
    

    print("\n".join([str(num) for num in qsort(heights) if num != 0]))
    
solution()