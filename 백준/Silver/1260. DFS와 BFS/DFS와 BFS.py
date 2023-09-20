from collections import deque
N, M, V = map(int, input().split())
graph = [[] for _ in range(N)]
visited_bfs = [False for _ in range(N)]
visited_dfs = [False for _ in range(N)]
result_dfs = []
result_bfs = []

for i in range(M):
    first, second = map(int, input().split())
    graph[first-1].append(second)
    graph[second-1].append(first)

def dfs(V):
    visited_dfs[V-1] = True
    result_dfs.append(V)

    for x in graph[V-1]:
        if visited_dfs[x-1] == False:
            dfs(x)

def bfs(V):
    queue = deque([V])
    visited_bfs[V-1] = True
    while(queue):
        x = queue.popleft()
        result_bfs.append(x)

        for i in graph[x-1]:
            if visited_bfs[i-1] == False:
                visited_bfs[i-1] = True
                queue.append(i)

for x in graph:
    x.sort()

dfs(V)
bfs(V)

for x in result_dfs:
    print(x, end= ' ')
print()
for x in result_bfs:
    print(x, end=' ')