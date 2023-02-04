from collections import deque
import sys

input = sys.stdin.readline

n, d, k, c = map(int, input().rstrip().split(" "))
sushi = [int(input()) for _ in range(n)]
plates = deque(sushi[:k])
count = len(set([*plates,c]))

i = n // 2 - 1 # 중간 인덱스
for _ in range(n):
    i += 1
    if i == n:
        i = 0
    plates.popleft()
    plates.append(sushi[i])
    unique = set([*plates,c])
    count = max(count, len(unique))
    
    if (count == k + 1):
        break
    
print(count)
    