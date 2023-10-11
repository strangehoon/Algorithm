from collections import deque
N, K = map(int, input().split())
visited = [-1] * 200001

queue = deque([N])
visited[N] = 0
while queue:
    x = queue.popleft()
    if x == K:
        print(visited[x])
        break
    if 0 <= x-1 < 200000:
        if visited[x-1] == -1:
            visited[x-1] = visited[x] + 1
            queue.append(x-1)
    if 0 <= x + 1 <= 200000:
        if visited[x+1] == -1:
            visited[x+1] = visited[x] + 1
            queue.append(x+1)
    if 0 <= x * 2 <= 200000:
        if visited[x*2] == -1:
            visited[x*2] = visited[x] + 1
            queue.append(x*2)