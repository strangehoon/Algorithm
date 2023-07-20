from collections import deque
import sys
N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
result = [-1 for i in range(N+1)]

for i in range(1, M+1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
result[X] = 0
queue = deque([X])
flag = 0
while(queue):
    r = queue.popleft()
    for s in graph[r]:
        if result[s] == -1:
            result[s] = result[r] + 1
            queue.append(s)


for i in range(1, N+1):
    if result[i] == K:
        flag = 1
        print(i)

if flag == 0:
    print(-1)