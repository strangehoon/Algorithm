from collections import deque
import sys
N, M, K = map(int, input().split())
graph = [[0]*M for _ in range(N)]
for i in range(K):
    a,b = map(int, sys.stdin.readline().split())
    graph[a-1][b-1] = 1

# 동 서 남 북
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def bfs(x,y):
    queue = deque([(x,y)])
    count = 1
    graph[x][y] = 0
    while(queue):
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < N and 0<= ny < M:
                if graph[nx][ny] == 1:
                    queue.append((nx,ny))
                    graph[nx][ny] = 0
                    count += 1
    return count
max = 0
for x in range(N):
    for y in range(M):
        if graph[x][y] == 1:
            count = bfs(x,y)
            if max < count:
                max = count

print(max)