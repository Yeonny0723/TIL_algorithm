import sys

input = sys.stdin.readline

def getCutLen(height): # 높이에 따라 잘라진 나무 길이 
    cut = 0
    for tree in trees:
        if tree > height:
            cut += (tree-height)
    return cut

def binary_search(start, end):
    if getCutLen(end) >= need:
        return end
    if start >= end:
        return binary_search(start-1, end)
    
    half = (start + end) // 2 + 1 if (start + end) % 2 != 0 else (start + end) // 2 
    cut = getCutLen(half)
    if cut == need: # 필요한 양과 같다면 그때 높이가 최대 
        return half
        
    elif cut > need: # 필요한 양 보다 많다면 높이를 더 올릴 수 있음
        return binary_search(half+1, end)
        
    else: # 필요한 양 보다 적다면 높이를 줄여야함
        return binary_search(start, half-1)

treeCount, need = map(int, input().rstrip().split(" "))
trees = list(map(int, input().rstrip().split(" ")))
height = max(trees) # 가능한 최대 높이에서 절반씩 나누며 
print(binary_search(0, height))