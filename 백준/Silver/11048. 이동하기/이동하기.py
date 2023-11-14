N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

result = [[0]*M for _ in range(N)]

dx = [0, -1, -1]
dy = [-1, -1, 0]

for x in range(N):
    for y in range(M):
        tem = [0]
        for i in range(3):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<M:
                tem.append(graph[nx][ny])
        graph[x][y] += max(tem)
print(graph[x][y])