N, M = map(int ,input().split())
visited = [False] * N
answer = []
def dfs(S, lst):
    if S == M:
        answer.append(lst)
        return
    for i in range(1, N+1):
        if not visited[i-1]:
            visited[i-1] = True
            dfs(S+1, lst + [i])
            visited[i-1] = False

dfs(0, [])
for x in answer:
    print(*x)