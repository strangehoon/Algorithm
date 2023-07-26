import sys
sys.setrecursionlimit(10000)
n = int(input())
result = []
def dfs(y, x):
    if graph[y][x] == 1:
        graph[y][x] = 0
        # 주변 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= a or ny < 0 or ny >= b:
                continue
            dfs(ny, nx)
        return True
    return False

for q in range(n):
    # 세팅 작업
    a, b, c = map(int, input().split())
    graph = [[0 for _ in range(a)] for _ in range(b)]
    for i in range(c):
        x, y = map(int, input().split())
        graph[y][x] = 1

    # 동 서 남 북
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    count = 0
    for i in range(a):
        for j in range(b):
            if dfs(j, i) == True:
                count += 1
    result.append(count)
for i in result:
    print(i)