from collections import deque
N, K = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))
S, X, Y = map(int, input().split())

queue = deque()


# 초기 큐 설정
for k in range(1, K+1):
    for i in range(N):
        for j in range(N):
            if graph[i][j] == k:
                queue.append((i,j,graph[i][j]))


# 동, 서, 남, 북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def bfs(queue):
    x,y,v = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<N and graph[nx][ny] == 0:
            graph[nx][ny] = v
            queue.append((nx,ny,v))

for i in range(S):
    for j in range(len(queue)):
        bfs(queue)

print(graph[X-1][Y-1])