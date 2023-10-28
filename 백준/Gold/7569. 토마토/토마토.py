from collections import deque
import sys
M, N, H = map(int, input().split())
graph = []
queue = deque()
for i in range(H):
    t = []
    for j in range(N):
        t.append(list(map(int, sys.stdin.readline().split())))
        for k in range(M):
            if t[j][k] == 1:
                queue.append((i,j,k))
    graph.append(t)

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

while queue:
    z,y,x = queue.popleft()
    for i in range(6):
        nz = z + dz[i]
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<=nz<H and 0<=ny<N and 0<=nx<M:
            if graph[nz][ny][nx] == 0:
                graph[nz][ny][nx] = graph[z][y][x] + 1
                queue.append((nz,ny,nx))
max_value = -10
for i in range(H):
    for j in range(N):
        max_value = max(max_value, max(graph[i][j]))
        for k in range(M):
            if graph[i][j][k] == 0:
                print(-1)
                exit(0)

if max_value == 1:
    print(0)
else:
    print(max_value-1)