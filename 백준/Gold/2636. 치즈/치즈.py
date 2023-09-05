from collections import deque
import sys

a, b = map(int, input().split())
graph = []
for i in range(a):
    graph.append(list(map(int, sys.stdin.readline().split())))

# 동, 서, 남, 북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs():
    count = 0
    queue = deque([(0,0)])
    while(queue):
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<a and 0<=ny<b:
                if graph[nx][ny] == 0 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                if graph[nx][ny] == 1 and visited[nx][ny] == False:
                    graph[nx][ny] = 0
                    visited[nx][ny] = True
                    count += 1
    return count

result = 0
data = []
while(True):
    visited = [[False] * b for _ in range(a)]
    count = bfs()
    data.append(count)
    if count == 0:
        break
    result += 1
print(result)
print(data[-2])