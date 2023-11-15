N, M = map(int, input().split())
result = []
def dfs(n, s, lst):
    if n == M:
        result.append(lst)
    for i in range(s, N+1):
        dfs(n+1, i+1, lst+[i])

dfs(0, 1, [])
for i in result:
    print(*i)