from itertools import combinations
N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

# 2차원 그래프에서 0인 값 3개의 좌표 조합 구하기
temp = [ (x,y) for x in range(N) for y in range(M) if graph[x][y] == 0]
data = list(combinations(temp, 3))

# 동 서 남 북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def dfs(graph, x, y, t):
    count = 1
    t[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < N and 0<= ny < M and graph[nx][ny] ==0 and t[nx][ny] == 0:
            count += dfs(graph, nx, ny, t)
    return count



result = 0
for i in data:
    t = [[0 for i in range(M)] for i in range(N)]
    count = 0
    safe = M*N

    # 벽 3개 세우기
    for j in range(3):
        x, y = i[j]
        graph[x][y] =1

    # 안전 구역 개수 구하기
    for j in range(N):
        for k in range(M):
            if graph[j][k] == 1:
                safe += -1
            if graph[j][k] == 2:
                count += dfs(graph, j,k,t)
    safe -= count

    # 안전 구역 최대값 구하기
    if safe > result:
        result = safe

    # graph 초기화
    for k in range(3):
        x, y = i[k]
        graph[x][y] = 0

print(result)