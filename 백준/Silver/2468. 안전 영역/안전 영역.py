from collections import deque
N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

# 최대닶, 최소값 찾기
min_value = 101
max_value = 0
for i in graph:
    if max(i) > max_value:
        max_value = max(i)
    if min(i) < min_value:
        min_value = min(i)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x,y,c,visited):
    visited[x][y] = True
    queue = deque([[x,y]])
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                if visited[nx][ny] == False and graph[nx][ny] > c:
                    visited[nx][ny] = True
                    queue.append([nx,ny])


result = 0
for c in range(min_value, max_value+1):
    count = 0
    visited = [[False] * N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if visited[x][y] == False and graph[x][y] > c:
                bfs(x,y,c,visited)
                count += 1

    if count > result:
        result = count
if result == 0:
    print(1)
else:
    print(result)