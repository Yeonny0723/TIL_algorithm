"""
인접한 수의 차이가 1인 수를 계단수라 부름.
숫자 n이 주어질 때, 길이가 n인 계단 수의 개수를 구하는 문제.

출력>
정답을 10^9로 나눈 나머지 출력
"""

n = int(input())
dp = [[0]*10 for _ in range(n+1)]  # dp[자리수][이전값] 가능한 개수
MOD = 10**9
for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, n+1):  # 자리수
    for j in range(10):  # 현재값
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n]) % MOD)