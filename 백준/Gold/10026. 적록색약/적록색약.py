from collections import deque
N = int(input())
graph = []
for i in range(N):
    graph.append(list(input()))

visited1 = [[False] * N for i in range(N)]
visited2 = [[False] * N for i in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs1(x,y,color):
    queue1 = deque([(x,y)])
    while queue1:
        x,y = queue1.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N:
                if graph[nx][ny] == color and visited1[nx][ny] == False:
                    visited1[nx][ny] = True
                    queue1.append((nx, ny))
    return 1

def bfs2(x,y,color):
    queue2 = deque([(x,y)])
    while queue2:
        x,y = queue2.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N:
                if color != 'B':
                    if graph[nx][ny] != 'B' and visited2[nx][ny] == False:
                        visited2[nx][ny] = True
                        queue2.append((nx, ny))
                else:
                    if graph[nx][ny] == 'B' and visited2[nx][ny] == False:
                        visited2[nx][ny] = True
                        queue2.append((nx,ny))
    return 1

count1 = 0
for x in range(N):
     for y in range(N):
         color = graph[x][y]
         if visited1[x][y] == False:
             count1 += bfs1(x,y,color)

count2 = 0
for x in range(N):
    for y in range(N):
        color = graph[x][y]
        if visited2[x][y] == False:
            count2 += bfs2(x,y,color)

print(count1)
print(count2)