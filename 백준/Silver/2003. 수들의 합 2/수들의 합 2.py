import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

total = a[0]
count, start, end = 0, 0, 1

while True:
    if total > m: # 크다면 맨 앞 숫자 제거
        total -= a[start]
        start += 1
    elif total < m: # 작다면 맨 뒤 숫자 추가
        if end < n:
            total += a[end]
            end += 1
        else:
            break
    else: # 동일하다면 count + 1 후 시작점 
        count += 1
        total -= a[start]
        start += 1

print(count)