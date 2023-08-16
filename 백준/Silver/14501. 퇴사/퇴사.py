n = int(input())

data = []
data.append([0,0])
for _ in range(n):
    data.append(list(map(int, input().split())))

dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    t = data[i][0]
    p = data[i][1]
    if dp[i] < dp[i-1]:
        dp[i] = dp[i-1]
    if i + t -1 <= n:
        dp[i+t-1] = max(dp[i+t-1], dp[i-1] + p)
print(dp[n])