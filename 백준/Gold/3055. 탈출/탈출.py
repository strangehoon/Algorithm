from collections import deque
import sys
R, C = map(int, input().split())
graph = []
for _ in range(R):
    graph.append(list(sys.stdin.readline()))
water_minute = [[10e9] * C for _ in range(R)]

# 동 서 남 북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def water_bfs(x, y, visited):
    water_minute[x][y] = 0
    queue = deque([(x,y)])
    while(queue):
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<R and 0<=ny<C and graph[nx][ny] == '.' and visited[nx][ny] == False:
                queue.append((nx,ny))
                visited[nx][ny] = True
                if water_minute[nx][ny] > water_minute[x][y] +1:
                    water_minute[nx][ny] = water_minute[x][y] + 1

def animal_bfs(x, y, visited2):
    water_minute[x][y] = 0
    queue2 = deque([(x, y, 1)])
    while (queue2):
        x, y, count = queue2.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] != '*' and graph[nx][ny] != 'X' and visited2[nx][ny] == False and water_minute[nx][ny] > count:
                if graph[nx][ny] == 'D':
                    return count
                visited2[nx][ny] = True
                queue2.append((nx, ny, count + 1))
    return "KAKTUS"

for i in range(R):
    for j in range(C):
        visited = [[False] * C for _ in range(R)]
        if graph[i][j] == '*':
            water_bfs(i, j, visited)
        # 시작 좌표 조회
        if graph[i][j] == 'S':
            S_x, S_y = i, j
visited2 = [[False] * C for _ in range(R)]
print(animal_bfs(S_x, S_y,visited2))