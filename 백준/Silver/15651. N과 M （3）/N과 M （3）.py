N, M = map(int, input().split())
visited = [False] * N
result = []
def dfs(c, t_list):
    if c == M:
        result.append(t_list)
        return
    for i in range(1, N+1):
        dfs(c+1, t_list + [i])

dfs(0, [])
for i in result:
    print(*i)