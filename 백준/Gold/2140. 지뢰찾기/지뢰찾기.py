n = int(input())
graph = []
for _ in range(n):
    graph.append(list(input()))

# 12시부터 시계방향
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
count = 0
def bomb(x, y):
    for i in range(8):
        nx = x+dx[i]
        ny = y+dy[i]
        if graph[nx][ny] != '#' and graph[nx][ny] != 'bomb':
            graph[nx][ny] = str(int(graph[nx][ny])-1)

for x in range(n):
    for y in range(n):
        flag = 0
        if graph[x][y] == '#':
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if graph[nx][ny] =='0':
                    flag = 1
                    break
            if flag == 0:
                bomb(x, y)
                graph[x][y] = 'bomb'
                count += 1

print(count)
