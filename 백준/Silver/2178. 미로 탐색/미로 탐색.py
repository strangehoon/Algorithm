from collections import deque
N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))
visited = [[False]*M for _ in range(N)]

# 동 서 남 북
dx = [0, 0, 1, -1]
dy = [1, -1, 0 ,0]
def bfs():
    queue = deque([(0,0,1)])
    visited[0][0] = True

    while(queue):
        x,y,c = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx == N-1 and ny ==M-1:
                print(c+1)
                return
            if 0<=nx<N and 0<=ny<M:
                if graph[nx][ny]==1 and visited[nx][ny] ==False:
                    visited[nx][ny] = True
                    queue.append((nx,ny,c+1))

bfs()