import sys

input = sys.stdin.readline

def dfs():
    global vowelsCount
    if len(pw) == L:
        if vowelsCount >= 1: # 모음 1개 이상 
            ans = ""
            for idx in pw:
                ans += lst[idx]
            print(ans)
        return
    
    for idx in range(C):
        if idx in pw: # 이미 뽑은 원소 중복 X
            continue
        if pw and idx < pw[-1]: # 알파벳 증가순으로 제한
            continue
        if lst[idx] in vowels:
            vowelsCount += 1
        if vowelsCount > L - 2: # 최대 모음 개수 L-2
            vowelsCount -= 1
            continue 
        pw.append(idx)
        dfs()
        if lst[idx] in vowels:
            vowelsCount -= 1
        pw.pop()

pw, vowels,vowelsCount = [], ["a", "e", "i", "o", "u"], 0
L, C = map(int, input().rstrip().split(" "))
lst = sorted(input().rstrip().split(" ")) # 정렬
dfs()

