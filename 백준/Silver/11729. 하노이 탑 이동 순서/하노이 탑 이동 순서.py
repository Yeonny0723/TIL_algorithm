import sys

input = sys.stdin.readline

def hanoi(n, start, rest, end): #  n 원반 개수, start 시작, rest 나머지, end 도착
    if n <= 1:
        move.append((start, end))
        return
    hanoi(n - 1, start, end, rest)
    move.append((start, end))
    hanoi(n - 1, rest, start, end)
    
k = int(input())
start, rest, end = 1,2,3
move = []
hanoi(k, start, rest, end)

print(len(move))
for el in move:
    print(*el)