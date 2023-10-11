from collections import deque
F, S, G, U, D = map(int, input().split())
visited = [-1] * (F+1)

queue = deque([S])
visited[S] = 0
while queue:
    x = queue.popleft()
    if x == G:
        print(visited[x])
        exit(0)
    if 1<=x+U<=F:
        if visited[x+U] == -1:
            visited[x+U] = visited[x] + 1
            queue.append(x+U)
    if 1<=x-D<=F:
        if visited[x-D] == -1:
            visited[x-D] = visited[x] + 1
            queue.append(x-D)

print("use the stairs")