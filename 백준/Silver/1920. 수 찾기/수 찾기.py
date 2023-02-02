import sys

input = sys.stdin.readline

def binary_search(start, end, target):
    if start >= end:
        if A[start] == target:
            return 1
        else: 
            return 0
            
    mid = (start+end) // 2
    if A[mid] == target:
        return 1
    if A[mid] > target:
        return binary_search(0, mid-1, target)
    if A[mid] < target:
        return binary_search(mid+1, end, target)  
    
n = int(input())
A = list(map(int, input().rstrip().split(" ")))
m = int(input())
M = list(map(int, input().split(" ")))
A.sort()
for num in M:
    print(binary_search(0, n-1, num))