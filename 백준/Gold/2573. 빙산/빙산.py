import sys,copy
from collections import deque
N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))
result = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def bfs(x,y,visited):
    queue = deque([(x,y)])
    visited[x][y] = True
    tem = [[0]*M for _ in range(N)]
    while queue:
        x,y = queue.popleft()
        count = 0
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if graph[nx][ny] != 0 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                elif graph[nx][ny] == 0:
                    count += 1
        tem[x][y] = max(0, graph[x][y] - count)
    return tem, visited

while(True):
    visited = [[False] * M for _ in range(N)]
    flag = False
    for x in range(N):
        for y in range(M):
            if graph[x][y] != 0 and not visited[x][y] and flag == False:
                tem, visited = bfs(x,y,visited)
                flag = True
            elif graph[x][y] != 0 and not visited[x][y] and flag == True:
                print(result)
                exit(0)
    # 빙산이 다 녹을때까지 분리되지 않는 경우
    if flag == False:
        print(0)
        exit(0)
    graph = copy.deepcopy(tem)
    result += 1
print(result)