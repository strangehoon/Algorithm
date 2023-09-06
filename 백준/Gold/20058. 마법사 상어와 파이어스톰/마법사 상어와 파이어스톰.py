import sys
from collections import deque
n, q = map(int, input().split())
graph = []

for i in range(2**n):
    graph.append(list(map(int, sys.stdin.readline().split())))
L = list(map(int, input().split()))

count = 0
total = 0
visited = [[False] * 2 ** n for _ in range(2 ** n)]

# 동,서,남,북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def rotate(x,y,w):
    tem_graph = [[0]*w for _ in range(w)]
    for i in range(w):
        for j in range(w):
            tem_graph[j][w-1-i] = graph[x+i][y+j]
    for i in range(w):
        for j in range(w):
            graph[x+i][y+j] = tem_graph[i][j]
def melt():
    tem = []
    for x in range(2**n):
        for y in range(2**n):
            count = 0
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0<=nx<2**n and 0<=ny<2**n:
                    if graph[nx][ny] != 0:
                        count += 1
            if count < 3 and graph[x][y] > 0:
                tem.append((x,y))
    for i in tem:
        graph[i[0]][i[1]] -= 1

def bfs(x,y):
    queue = deque([(x,y)])
    visited[x][y] = True
    count = 0
    while(queue):
        count += 1
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<2**n and 0<=ny<2**n:
                if graph[nx][ny] != 0 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
    return count

def firestorm(L):
    w = 2**L
    for i in range(0, 2**n, w):
        for j in range(0, 2**n, w):
            rotate(i,j,w)
    melt()

# main
for i in L:
    firestorm(i)

for x in range(2**n):
    for y in range(2**n):
        if graph[x][y] != 0:
            if visited[x][y] == False:
                count = max(count, bfs(x,y))
            total += graph[x][y]
print(total)
print(count)