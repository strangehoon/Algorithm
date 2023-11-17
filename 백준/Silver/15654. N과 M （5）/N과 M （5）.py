N, M = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

visited = [False]*N
result = []
def dfs(c, l_list):
    if c == M:
        result.append(l_list)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dfs(c+1, l_list + [data[i]])
            visited[i] = False

dfs(0, [])
for i in result:
    print(*i)