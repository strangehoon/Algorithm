from collections import deque
import sys

h, w = map(int, input().split())
graph = []
for i in range(h):
    graph.append(list(sys.stdin.readline()))

# 동, 서, 남, 북
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y):
    visited = [[-1] * w for _ in range(h)]
    queue = deque([(x,y,0)])
    visited[x][y] = 0
    while queue:
        x,y,c = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<h and 0<=ny<w:
                if graph[nx][ny] == 'L' and visited[nx][ny] == -1:
                    visited[nx][ny] = c+1
                    queue.append((nx,ny,c+1))
    return c

result = 0
for x in range(h):
    for y in range(w):
        if 0<x<h-1:
            if graph[x-1][y] == 'L' and graph[x+1][y] == 'L':
                continue
        if 0<y<w-1:
            if graph[x][y-1] == 'L' and graph[x][y+1] =='L':
                continue
        if graph[x][y] == 'L':
            if result < bfs(x,y):
                result = bfs(x,y)
print(result)
