import sys

input = sys.stdin.readline

# 파이썬에는 switch - case 문이 없어서 비슷하게 딕셔너리로 구현해봄 
def push(res, num):
    res.append(num)
    return res
    
def pop(res):
    if res:
        print(res.pop())
    else:
        print(-1)
    return res
    
def size(res):
    print(len(res))
    return res

def empty(res):
    if res:
        print(0)
    else:
        print(1)  
    return res
        
def top(res):
    if res:
        print(res[-1])
    else:
        print(-1) 
    return res


cmd_dict = {
    "push": push,
    "pop": pop,
    "size": size,
    "empty": empty,
    "top": top
}


N = int(input())
res = []
for _ in range(N):
    cmd = input().rstrip().split()
    if len(cmd) == 1:
        action = cmd[0]
        res = cmd_dict[action](res)
    else:
        action, num = cmd
        res = cmd_dict[action](res, num)