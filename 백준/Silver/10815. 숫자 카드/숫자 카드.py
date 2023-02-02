import sys

input = sys.stdin.readline

def binary_search(start, end, target):
    if start >= end:
        if N[start] == target:
            return 1
        else:
            return 0
        
    mid = (start+end) // 2
    if N[mid] == target:
        return 1
    if N[mid] > target:
        return binary_search(0, mid-1, target)
    else: 
        return binary_search(mid+1, end, target)

n = int(input())
N = list(map(int, input().rstrip().split(" ")))
N.sort() # nlogn
m = int(input())
M = list(map(int, input().rstrip().split(" ")))
ans = []
for num in M: # n
    ans.append(str(binary_search(0, n-1, num))) # logn
print(" ".join(ans))
