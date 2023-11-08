N, S = map(int, input().split())
data = list(map(int, input().split()))
visited = [False] * N
result = 0
def dfs(s, p):
    global result
    if s == S:
        result += 1
    for i in range(p+1, N):
        if not visited[i]:
            visited[i] = True
            dfs(s+data[i], i)
            visited[i] = False

for i in range(N):
    visited[i] = True
    dfs(data[i], i)
print(result)