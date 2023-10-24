from collections import deque
n = int(input())
x,y = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque([[x, 1]])
visited[x] = True
while queue:
    s, c = queue.popleft()
    for i in graph[s]:
        if visited[i] == False:
            if i == y:
                print(c)
                exit(0)
            visited[i] = True
            queue.append([i, c+1])
    c += 1
print(-1)
