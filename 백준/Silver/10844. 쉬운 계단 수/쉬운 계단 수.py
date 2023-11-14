N = int(input())
dp = [[0]*11 for _ in range(N)]
for i in range(1, 10):
    dp[0][i] = 1
for i in range(1, N):
    for j in range(10):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
print(sum(dp[N-1])%1000000000)