a = list(input())
b = list(input())
dp = [[0]*(len(a)+1) for _ in range(len(b)+1)]

ans = 0
for j in range(1, len(a)+1):
    for i in range(1, len(b)+1):
        if a[j-1] == b[i-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        ans = max(ans, dp[i][j])
print(ans)