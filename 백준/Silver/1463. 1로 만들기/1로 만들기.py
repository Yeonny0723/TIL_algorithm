import sys

input = sys.stdin.readline

def solution():
    N = int(input())
    cache = [0] * (N+1)

    for i in range(2, N+1): # f(0), f(1) = 0,0이므로
        cache[i] = cache[i-1] + 1 # -1
        if i % 2 == 0:
            cache[i] = min(cache[i], cache[i//2] + 1)
        if i % 3 == 0:
            cache[i] = min(cache[i], cache[i//3] + 1)
    print(cache[N])
    
solution()