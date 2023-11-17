N, M = map(int, input().split())
visited = [False] * N
result = []
a = 1
def dfs(count, x, l_list):
    if count == M:
        result.append(l_list)
        return
    for i in range(x, N+1):
        dfs(count+1, i, l_list + [i])

dfs(0, 1, [])
for i in result:
    print(*i)