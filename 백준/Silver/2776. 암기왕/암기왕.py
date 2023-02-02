import sys

input = sys.stdin.readline

def binary_search(start, end, target):
    if start >= end:
        if N1[start] == target:
            return 1
        else: 
            return 0
            
    mid = (start+end) // 2
    if N1[mid] == target:
        return 1
    if N1[mid] > target:
        return binary_search(0, mid-1, target)
    if N1[mid] < target:
        return binary_search(mid+1, end, target)  
    
for _ in range(int(input())):
    n1 = int(input())
    N1 = list(map(int, input().rstrip().split(" ")))
    n2 = int(input())
    N2 = list(map(int, input().rstrip().split(" ")))
    N1.sort()
    for num in N2:
        print(binary_search(0, n1-1, num))