# 방법 1. 
import sys

input = sys.stdin.readline

N = int(input())
res = []
for _ in range(N):
    cmd = input().split()
    action, num = None, None
    
    if len(cmd) == 1:
        action = cmd[-1]
    else: 
        action, num = cmd
        
    if action == 'push':
        res.append(num)
        
    elif action == 'pop':
        if res:
            print(res.pop())
        else:
            print(-1)
    elif action == 'size':
        print(len(res))
    elif action == 'empty':
        if res:
            print(0)
        else:
            print(1)
    elif action == 'top':
        if res:
            print(res[-1])
        else:
            print(-1)