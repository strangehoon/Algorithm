from collections import deque
N, K = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))
S, X, Y = map(int, input().split())

# 초기 큐 설정
data = []
for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            data.append((graph[i][j], i, j))
data.sort()
queue = deque(data)

# 동, 서, 남, 북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def bfs(queue):
    v, x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<N and graph[nx][ny] == 0:
            graph[nx][ny] = v
            queue.append((v, nx, ny))

for i in range(S):
    for j in range(len(queue)):
        bfs(queue)

print(graph[X-1][Y-1])