import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    res = []
    s = input().rstrip()
    for ch in s:
        if res:
            if (ch == ')') and (res[-1] == '('):
                res.pop()
                continue    
        res.append(ch)
    if res:
        print("NO")
    else:
        print("YES")