R, C = map(int, input().split())
visited = [0] * 26
graph = []
for _ in range(R):
    graph.append(list(input()))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
max_value = 0
visited[ord(graph[0][0])-65] = 1
def dfs(x,y,c):
    global max_value
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<R and 0<=ny<C:
            if visited[ord(graph[nx][ny])-65] == 0:
                visited[ord(graph[nx][ny])-65] = 1
                dfs(nx,ny,c+1)
                visited[ord(graph[nx][ny])-65] = 0
    max_value = max(max_value, c)

dfs(0,0,1)
print(max_value)
