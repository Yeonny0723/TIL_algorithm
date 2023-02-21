"""
       i
[] [] [o] [] []

풀이
경우의 수 나누기>
두가지 경우의 수에 최대값을 비교해 갱신시켜줄 수 있음.
- i-1이 선택된 경우 결과값:
i-3까지의 최대값 + i-1의 값 + i의 값
[x] [o] [o] [] []
- i-1이 선택되지 않고 i-2가 선택된 경우 결과값:
i-2가 선택되었을 때 최대값 + i의 값
[o] [x] [o] [] []:

점화식>
최대값을 저장하는 dp 배열 생성, 계단별 값을 담은 배열 arr
max(dp[i-3]+arr[i-1]+arr[i], dp[i-2]+arr[i])
"""
import sys

input = sys.stdin.readline

n = int(input())
arr = [0 for _ in range(301)]
dp = [0 for _ in range(301)]
for i in range(n):
    arr[i] = int(input())

dp[0] = arr[0]
dp[1] = arr[0] + arr[1]
dp[2] = max(arr[0]+arr[2], arr[1]+arr[2])

for i in range(3, n):
    dp[i] = max(dp[i-3]+arr[i-1]+arr[i], dp[i-2]+arr[i])

print(dp[n-1])