from collections import deque
import sys

input = sys.stdin.readline

q = deque()
for _ in range(int(input())):
    cmd = input().rstrip()
    if cmd == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif cmd == 'size':
        print(len(q))
    elif cmd == 'empty':
        if q: 
            print(0)
        else:
            print(1)
    elif cmd == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif cmd == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)
    else: # push
        action, num = cmd.split()
        q.append(int(num))