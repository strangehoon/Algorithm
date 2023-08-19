n = int(input())

data = list(map(int, input().split()))
dp = [1 for _ in range(len(data))]

data.reverse()

# 0 1 2 3 4 5 6
for i in range(n):
    for j in range(i):
        if data[j] < data[i]:
            dp[i] = max(dp[j] +1, dp[i])
print(n-max(dp))