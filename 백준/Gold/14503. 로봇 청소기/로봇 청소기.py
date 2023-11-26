import sys
N, M = map(int, input().split())
r, c, d = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited = [[False] * M for _ in range(N)]

def dfs(x, y, d, count):
    flag = True
    # 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
    if graph[x][y] == 0:
        graph[x][y] = 2
        count += 1
    for i in range(1, 5):
        nx = x+dx[(d-i)%4]
        ny = y+dy[(d-i)%4]
        if 0<=nx<N and 0<=ny<M and graph[nx][ny] == 0:
            dfs(nx, ny, (d-i)%4, count)
    nx = x+dx[(d+2)%4]
    ny = y+dy[(d+2)%4]
    if graph[nx][ny] != 1:
        dfs(nx, ny, d, count)
    if graph[nx][ny] == 1:
        print(count)
        exit(0)

dfs(r, c, d, 0)