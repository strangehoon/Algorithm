from collections import deque
import sys
N, M = map(int, input().split())
graph = []
for i in range(M):
    graph.append(list(map(int, sys.stdin.readline().split())))

queue = deque()
for x in range(M):
    for y in range(N):
        if graph[x][y] == 1:
            queue.append((x,y))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def bfs():
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<M and 0<=ny<N:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx,ny))

bfs()
max_value = -10
for x in range(M):
    for y in range(N):
        if graph[x][y] == 0:
            print(-1)
            exit(0)
    max_value = max(max_value, max(graph[x]))
if max_value == 1:
    print(0)
else:
    print(max_value-1)