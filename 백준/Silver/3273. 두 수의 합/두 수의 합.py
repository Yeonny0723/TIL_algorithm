import sys

input = sys.stdin.readline

n = int(input()) # 수열 크기
a = list(map(int, input().rstrip().split(" "))) # 수열
x = int(input()) # 만들어야하는 값
a.sort() # 정렬
count = 0
start, end = 0, n-1
total = a[start] + a[end]

while start < end:
    if total < x:
        start += 1
    elif total > x:
        end -= 1
    else:
        count += 1
        start += 1
    total = a[start] + a[end]

print(count)
