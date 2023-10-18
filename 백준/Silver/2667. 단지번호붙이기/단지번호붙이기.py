N = int(input())
graph = []
result = []
visited = [[False] * N for _ in range(N)]
for i in range(N):
    graph.append(list(map(int, input())))

# 동, 서, 남, 북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def dfs(x,y,c):
    graph[x][y] = 0
    visited[x][y] = True
    c += 1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<= nx < N and 0<= ny < N:
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                c = dfs(nx,ny,c)
    return c
for x in range(N):
    for y in range(N):
        if graph[x][y] != 0:
            count = dfs(x,y,0)
            result.append(count)

print(len(result))
result.sort()
for s in result:
    print(s)